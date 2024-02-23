from odoo import models, fields, api


class SearchCustomer(models.Model):
    _name = "search.customer"
    _description = "task"

    name = fields.Many2one('res.partner', string="Name")
    phone = fields.Char(string="phone")
    email = fields.Char(string="Email")

    def sale_order_submit_button(self):
        print(self.name.id, "=====================")
        # return {
        #     'name': 'Customer',
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'res.partner',
        #     'view_id': self.env.ref('base.view_partner_form').id,
        #     'view_mode': 'form',
        #     'view_type': 'form',
        #     'domain': [('name', '=', self.name.name)],
        #     'target': 'current'}
        return {
            'name': "customer",
            'view_mode': 'form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'res_id': self.name.id
            # 'domain': [('id', 'in', self.name.id)]
        }
