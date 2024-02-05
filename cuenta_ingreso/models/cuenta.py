from odoo import models, fields, api, exceptions, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    income_account_id = fields.Many2one('account.account', string='Cuenta de Ingreso', domain=[('account_type', '=', 'income')], options={'no_create': True}, groups="account.group_account_readonly")


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    is_sale_order = fields.Boolean(string='Es una venta', compute='_compute_is_sale_order', store=True)

    @api.depends('invoice_origin')
    def _compute_is_sale_order(self):
        for invoice in self:
            invoice.is_sale_order = bool(invoice.invoice_origin)


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    income_account_id = fields.Many2one(
        'account.account',
        string='Cuenta de Ingreso del Cliente',
        related='order_id.partner_id.income_account_id',
        store=True,
        readonly=False,
    )


class AccountInvoiceLine(models.Model):
    _inherit = 'account.move.line'

    @api.onchange('partner_id', 'product_id')
    def _onchange_partner_id(self):
        if self.move_id:
            # Verificar si el documento es una factura de cliente o una nota de crédito de cliente
            if self.move_id.move_type in ['out_invoice', 'out_refund']:
                if move_id.is_sale_order:
                    # Si es una venta, copiar la cuenta de ingreso del cliente al campo account_id
                   account_id = move_id.partner_id.income_account_id
                elif self.partner_id and self.display_type not in ['line_section', 'line_note']:
                    # Si no es una venta, aplicar la lógica original
                    income_account = self.partner_id.income_account_id
                    if income_account:
                        self.account_id = income_account
                    else:
                        raise exceptions.UserError(_("Por favor, seleccione una cuenta de ingreso para este contacto antes de guardar la factura."))
                else:
                    # Si es una línea de sección o nota, no aplicar la lógica de cuenta de ingresos
                    self.account_id = False
