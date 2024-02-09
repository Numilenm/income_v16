from odoo import models, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.depends('move_id')
    def _compute_account_id(self):
        super()._compute_account_id()  # Llamar a la implementación original

        for line in self:
            if line.move_id and line.move_id.move_type in ['out_invoice', 'out_refund'] and line.sale_line_ids:
                sale_order = line.sale_line_ids[0]  # Obtener la primera orden de venta asociada
                if sale_order:
                    line.account_id = sale_order.partner_income_account_id
