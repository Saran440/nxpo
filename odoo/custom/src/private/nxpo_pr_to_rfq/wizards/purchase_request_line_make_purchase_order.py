# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):
    _inherit = "purchase.request.line.make.purchase.order"

    order_type = fields.Many2one(
        comodel_name="purchase.order.type",
        string="Order Type",
    )
    num_installment = fields.Integer(
        string="Period",
    )

    @api.constrains("num_installment")
    def _constrains_num_installment(self):
        for record in self:
            if record.num_installment <= 0:
                raise UserError(_("Period must be greater than zero"))

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        active_model = self.env.context.get("active_model", False)
        active_ids = self.env.context.get("active_ids", False)

        _dict = {
            "purchase.request.line": "request_id.num_installment",
            "purchase.request": "num_installment",
        }
        num_installments = list(
            dict.fromkeys(
                self.env[active_model].browse(active_ids).mapped(_dict[active_model])
            )
        )

        if len(num_installments) == 1:
            to_contract = num_installments[0] > 1 and True or False
            domain = [("to_contract", "=", to_contract)]
            res["order_type"] = self.env["purchase.order.type"].search(domain, limit=1)
            res["num_installment"] = num_installments[0]
        else:
            raise UserError(_("You have to select lines from the same order type."))

        return res

    @api.onchange("num_installment")
    def _onchange_num_installment(self):
        to_contract = self.num_installment > 1
        domain = [("to_contract", "=", to_contract)]
        self.order_type = self.env["purchase.order.type"].search(domain, limit=1)

    @api.model
    def _prepare_purchase_order(self, picking_type, group_id, company, origin):
        data = super()._prepare_purchase_order(picking_type, group_id, company, origin)
        data.update(
            {
                "order_type": self.order_type.id,
                "num_installment": self.num_installment,
            }
        )
        return data
