# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _per_pfq_lines(self, rfqs):
        groups = {}
        for line in rfqs.mapped("order_line"):
            request_id = line.mapped("purchase_request_lines.request_id")
            key = (
                request_id,
                line.account_analytic_id,
                line.product_id,
                line.product_uom,
            )
            groups.setdefault(key, 0.0)
            groups[key] = line.product_qty

        lines = [(5, 0, 0)]
        for (
            _request_id,
            account_analytic_id,
            product_id,
            uom_id,
        ), qty in groups.items():
            line_vals = {
                "product_id": product_id.id,
                "product_qty": qty,
                "product_uom_id": uom_id.id,
                "account_analytic_id": account_analytic_id.id,
            }
            lines.append((0, 0, line_vals))
        tender_vals = {
            "line_ids": lines,
        }
        return tender_vals

    def action_create_tender(self):
        """
        1. create purchase.requisition (tender)
        2. assign tender to rfq
        3. return to tender form view
        """
        tender_obj = self.env["purchase.requisition"]
        purchase_obj = self.env["purchase.order"]

        if self._context.get("active_model", False) == "purchase.order":
            active_ids = self._context.get("active_ids", [])
        else:
            active_ids = self.ids

        domain = [
            ("id", "in", active_ids),
            ("requisition_id", "=", False),
            ("state", "not in", ["purchase", "done", "cancel"]),  # need?
        ]
        rfqs = purchase_obj.search(domain)
        if not rfqs:
            return

        # 1. create purchase.requisition (tender)
        tender_vals = self._per_pfq_lines(rfqs)
        tender = tender_obj.create(tender_vals)
        tender.action_in_progress()

        if tender:
            # 2. assign tender to rfq
            rfqs.update(
                {
                    "requisition_id": tender.id,
                    "origin": tender.name,
                }
            )

            # 3. return to tender form view
            action = self.env.ref(
                "purchase_requisition.action_purchase_requisition"
            ).read()[0]
            action["res_id"] = tender.id
            action["views"] = [
                (
                    self.env.ref(
                        "purchase_requisition.view_purchase_requisition_form"
                    ).id,
                    "form",
                )
            ]
        else:
            action = {"type": "ir.actions.act_window_close"}

        return action
