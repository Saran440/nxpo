# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    purchase_request_ids = fields.Many2many(
        "purchase.request",
        compute="_compute_purchase_request",
        string="Purchase Requests",
    )

    def _compute_purchase_request(self):
        for rec in self:
            rec.purchase_request_ids = rec.mapped(
                "order_line.purchase_request_lines.request_id"
            )
