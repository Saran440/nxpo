# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class BudgetTransferItem(models.Model):
    _inherit = "budget.transfer.item"

    target_department_id = fields.Many2one(
        comodel_name="hr.department", compute="_compute_target_department"
    )
    target_budget_control_id = fields.Many2one(
        comodel_name="budget.control",
        domain="[('budget_id', '=', mis_budget_id), "
        "('operating_unit_id', '=', target_operating_unit_id), "
        "('department_id', '=', target_department_id)]",
    )

    @api.depends("transfer_id")
    def _compute_target_department(self):
        Employee = self.env["hr.employee"]
        employee_id = Employee.search([("user_id", "=", self.env.user.id)])
        if not employee_id:
            raise UserError(
                _("%s is not related in Employee" % (self.env.user.display_name))
            )
        for rec in self:
            rec.target_department_id = employee_id.department_id or False
