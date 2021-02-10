# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class BudgetSourceFundLine(models.Model):
    _inherit = "budget.source.fund.line"

    department_id = fields.Many2one(
        comodel_name="hr.department",
        related="budget_control_id.department_id",
        store=True,
    )
