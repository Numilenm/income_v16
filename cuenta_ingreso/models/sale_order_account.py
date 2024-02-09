from odoo import models, fields, api, exceptions, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    partner_income_account_id = fields.Many2one('account.account', string='Cuenta de Ingreso del Cliente', compute='_compute_partner_income_account', store=True, readonly=True)

    @api.depends('order_id.partner_id')
    def _compute_partner_income_account(self):
        for line in self:
            if line.order_id.partner_id:
                line.partner_income_account_id = line.order_id.partner_id.income_account_id
            else:
                line.partner_income_account_id = False

    @api.constrains('order_id')
    def _check_partner_income_account(self):
        for line in self:
            if not line.partner_income_account_id:
                raise exceptions.ValidationError(_("Por favor, seleccione una cuenta de ingreso para el cliente asociado a esta orden de venta antes de continuar."))
