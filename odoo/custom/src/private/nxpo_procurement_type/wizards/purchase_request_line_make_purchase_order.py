# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):
    _inherit = "purchase.request.line.make.purchase.order"

    procurement_type_id = fields.Many2one(
        comodel_name="procurement.type",
        string="Procurement Type",
    )

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        active_model = self.env.context.get("active_model", False)
        active_ids = self.env.context.get("active_ids", False)
        _dict = {
            "purchase.request.line": "request_id.procurement_type_id",
            "purchase.request": "procurement_type_id",
        }
        type_ids = (
            self.env[active_model].browse(active_ids).mapped(_dict[active_model]).ids
        )

        if not type_ids:
            return res

        if len(type_ids) != 1:
            raise UserError(
                _("You have to select purchase request from the same procurement type.")
            )

        res["procurement_type_id"] = type_ids[0]
        return res

    @api.model
    def _prepare_purchase_order(self, picking_type, group_id, company, origin):
        data = super()._prepare_purchase_order(picking_type, group_id, company, origin)
        data.update(
            {
                "procurement_type_id": self.procurement_type_id.id,
            }
        )
        return data
