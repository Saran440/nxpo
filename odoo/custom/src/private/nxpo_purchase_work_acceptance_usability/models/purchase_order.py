# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    readonly_price = fields.Boolean(
        string="Readonly Price", compute="_compute_readonly_price"
    )

    def _compute_readonly_price(self):
        for rec in self:
            wa_states = rec.mapped("wa_line_ids").mapped("wa_id.state")
            if "accept" in wa_states or "draft" in wa_states:
                rec.readonly_price = True
            else:
                rec.readonly_price = False
