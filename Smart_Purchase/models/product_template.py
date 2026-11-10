from odoo import models , fields , api
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit ='product.template'

    sp_min_qty= fields.Integer(
        string='Minimum Quantity',
        help='Shows a reorder alert when stock reaches the minimum quantity.',
    )
    sp_reorder_qty=fields.Integer(
        string='Reorder Quantity',
        help='Number of units to order when stock is low.',
    )
    sp_needs_reorder=fields.Boolean(
        string='Needs Reorder',
        readonly=True
    )
    
    @api.model
    def _cron_update_sp_needs_reorder(self):
        products = self.search([('is_storable','=',True)])
        for product in products:
            if product.sp_min_qty > 0 and product.virtual_available <= product.sp_min_qty :
                product.sp_needs_reorder=True
            else:
                product.sp_needs_reorder=False

    def _sp_suggested_qty(self):
        self.ensure_one()
        missing=self.sp_min_qty - self.virtual_available
        return max(self.sp_reorder_qty,missing,1)


    def _sp_pending_order_lines(self):
        self.ensure_one()
        pending_reorders =self.env['purchase.order.line']
        lines =self.env['purchase.order.line'].search([(
            'product_id.product_tmpl_id', '=', self.id),
            ('order_id.state','in',['draft','sent','to approve','purchase'])
            ])
        for line in lines:
            if line.qty_received < line.product_qty:
                pending_reorders += line

        return pending_reorders
    def action_sp_create_po(self):
        self.ensure_one()
        offer=self.seller_ids.filtered('sp_is_best')[:1]
        if not offer:
            raise UserError('Please add at least one vendor on the Purchase tab first.')
        return offer.action_create_rfq()


