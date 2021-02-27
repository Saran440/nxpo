# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import _, models
from odoo.exceptions import UserError


class BudgetTransferItem(models.Model):
    _inherit = "budget.transfer.item"

    def _check_fund_constraint(self):
        for rec in self:
            source_fund_constraint = rec.source_budget_control_id.fund_constraint
            target_fund_constraint = rec.target_budget_control_id.fund_constraint
            source_program = source_fund_constraint.mapped("program_id").ids
            target_program = target_fund_constraint.mapped("program_id").ids
            if source_program != target_program:
                raise UserError(
                    _(
                        "{} and\n{}\nare different program.".format(
                            rec.source_budget_control_id.name,
                            rec.target_budget_control_id.name,
                        )
                    )
                )
