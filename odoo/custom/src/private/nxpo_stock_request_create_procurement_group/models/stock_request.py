# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockRequest(models.Model):
    _inherit = "stock.request"

    procurement_group_id = fields.Many2one(
        states={"draft": [("readonly", False)]},
        readonly=True,
        copy=False,
    )

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if not res.procurement_group_id and res.order_id:
            res.procurement_group_id = res.order_id.procurement_group_id
        return res
