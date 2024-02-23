from odoo import models, fields, api


class SaleOrderLines(models.Model):
    _inherit = "sale.order.line"
    _description = "task"

    discount_method = fields.Selection(
        [('fixed', "Fixed"),
         ('percentage', "Percentage"),
         ], string="Discount Method")
    discount_amount = fields.Float(
        string='Discount Amount'
    )
class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "task"

    discount_applies = fields.Selection(
        [
            ('order_line', "Order Line"),
            ('global', "Global"),
        ],
        required=True,
        string="Discount Applies To")

    discount_method = fields.Selection(
        [('fixed', "Fixed"),
         ('percentage', "Percentage"),
         ], string="Discount Method")
    discount_amount = fields.Float(
        string='Discount Amount'
    )
    discount = fields.Float(
        string='Discount'
    )
    def action_show_customer(self):
        return {
            'name': 'Customer',
            'type': 'ir.actions.act_window',
            'res_model': 'search.customer',
            'view_id': self.env.ref('global_discount.search_customer_from_view').id,
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
        }