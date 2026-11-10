from odoo import fields, models

class SpOrderWarning(models.TransientModel):
    _name = 'sp.order.warning'
    _description = 'Warning: open purchase orders exist'

    offer_id=fields.Many2one(
        'product.supplierinfo',
        required=True,
        ondelete='cascade')
    
    product_tmpl_id = fields.Many2one(
        related='offer_id.product_tmpl_id',
        string='Product')
    
    partner_id = fields.Many2one(
        related='offer_id.partner_id', 
        string='New Order Vendor')
    
    order_ids=fields.Many2many(
        'purchase.order',
        string='Existing Open Orders',
        readonly=True)
    
    pending_qty=fields.Integer(
        string='Quantity Already on Order',
        readonly=True)

    def action_confirm(self):
        self.ensure_one()

        return self.offer_id._sp_create_rfq()

    