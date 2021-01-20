# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"

    name = fields.Char(
        string="Request Reference",
        required=True,
        default="New",
        track_visibility="onchange",
    )

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("purchase.request")
        return super(PurchaseRequest, self).create(vals)
