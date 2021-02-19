# Copyright 2021 Ecosoft
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models


class RequestRequest(models.Model):
    _inherit = "request.request"

    def _prepare_hr_expense_line(self, line, sheet):
        line_vals = super()._prepare_hr_expense_line(line, sheet)
        line_vals.update(
            {
                "activity_id": line.activity_id.id,
            }
        )
        return line_vals

    def _prepare_purchase_request_line(self, line, purchase_request):
        line_vals = super()._prepare_purchase_request_line(line, purchase_request)
        line_vals.update(
            {
                "activity_id": line.activity_id.id,
            }
        )
        return line_vals
