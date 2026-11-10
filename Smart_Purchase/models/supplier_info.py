from odoo import models , fields , api ,Command


class ProductSupplierInfo(models.Model):
    _inherit='product.supplierinfo'

    sp_price_company = fields.Float(
    string='Price in EGP',
    compute='_compute_sp_price_company',
        )
    sp_is_best=fields.Boolean(
        string='Best Offer',
        compute='_compute_sp_is_best'
    )
    @api.depends('price','currency_id')
    def _compute_sp_price_company(self):
        egp = self.env.ref('base.EGP')
        company=self.env.company
        for offer in self:
            source_currency=offer.currency_id or company.currency_id
            offer.sp_price_company=source_currency._convert(
                offer.price,
                egp,
                company,
                fields.Date.today()
            )
    @api.depends(
        'price',
        'currency_id',
        'company_id',
        'delay',
        'product_tmpl_id.seller_ids.price',
        'product_tmpl_id.seller_ids.currency_id',
        'product_tmpl_id.seller_ids.company_id',
        'product_tmpl_id.seller_ids.delay',
    )
    def _compute_sp_is_best(self):
        for offer in self:
            offers = offer.product_tmpl_id.seller_ids
            best=min(
                offers,
                key=lambda vendor: (
                    vendor.sp_price_company,
                    vendor.delay,
                    vendor.id or 0,
                ),
                default=False,
            )
            offer.sp_is_best = (offer == best)

    def action_create_rfq(self):
        self.ensure_one()
        pending=self.product_tmpl_id._sp_pending_order_lines()
        if pending:
            caution=self.env['sp.order.warning'].create({
                'offer_id':self.id,
                'order_ids':[Command.set(pending.order_id.ids)],
                'pending_qty':sum(line.product_qty - line.qty_received for line in pending)
            })
            return{
                'type':'ir.actions.act_window',
                'name':'Warning: open orders exist',
                'res_model':'sp.order.warning',
                'res_id':caution.id,
                'view_mode': 'form',
                'target': 'new',
            }
        return self._sp_create_rfq()
    def _sp_create_rfq(self):
        self.ensure_one()
        product=self.product_id or self.product_tmpl_id.product_variant_id
        qty = max(self.min_qty, self.product_tmpl_id._sp_suggested_qty())
        order=self.env['purchase.order'].create({
            'partner_id': self.partner_id.id,
            'order_line': [Command.create({
                'product_id': product.id,
                'product_qty': qty,
            })],
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'res_id': order.id,
            'view_mode': 'form',
            }
