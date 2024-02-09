from odoo import models, fields, api, exceptions, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    income_account_id = fields.Many2one('account.account', string='Cuenta de Ingreso', domain=[('account_type', '=', 'income')], options={'no_create': True}, groups="account.group_account_readonly")


class AccountInvoiceLine(models.Model):
    _inherit = 'account.move.line'

    @api.onchange('partner_id', 'product_id')
    def _onchange_partner_id(self):
        if self.move_id and self.move_id.move_type in ['out_invoice', 'out_refund']:
            if self.partner_id and self.display_type not in ['line_section', 'line_note']:
                # Obtener la cuenta de ingresos asociada al cliente
                if self.move_id.sale_order_id:  # Si viene de una orden de venta
                    income_account = self.move_id.sale_order_id.partner_income_account_id
                else:
                    income_account = self.partner_id.income_account_id

                # Configurar la cuenta contable por defecto en función de la cuenta de ingresos del cliente
                if income_account:
                    self.account_id = income_account
                else:
                    raise exceptions.UserError(_("Por favor, seleccione una cuenta de ingreso para este contacto antes de guardar la factura."))
            else:
                # Si es una línea de sección o nota, no aplicar la lógica de cuenta de ingresos
                self.account_id = False
