# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import _, fields, models


class ResProgramAllocation(models.Model):
    _name = "res.program.allocation"
    _inherit = "mail.thread"
    _description = "Program for allocated"

    name = fields.Char(
        required=True,
        readonly=True,
        states={"draft": [("readonly", "=", False)]},
    )
    budget_period_id = fields.Many2one(
        comodel_name="budget.period",
        required=True,
        readonly=True,
        states={"draft": [("readonly", "=", False)]},
    )
    fund_constraint = fields.One2many(
        comodel_name="fund.constraint",
        inverse_name="program_allocation_id",
        context={"active_test": False},
        readonly=True,
        states={"draft": [("readonly", "=", False)]},
    )
    plan_id = fields.Many2one(comodel_name="budget.plan")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        default="draft",
        copy=False,
    )

    def action_done(self):
        return self.write({"state": "done"})

    def action_draft(self):
        return self.write({"state": "draft"})

    def action_cancel(self):
        return self.write({"state": "cancel"})

    def _prepare_vals_budget_plan(self):
        vals = {
            "name": self.name,
            "budget_period_id": self.budget_period_id.id,
        }
        return vals

    def action_generate_budget_plan(self):
        self.ensure_one()
        BudgetPlan = self.env["budget.plan"]
        vals = self._prepare_vals_budget_plan()
        plan_id = BudgetPlan.create(vals)
        self.write({"plan_id": plan_id.id})
        plan_id.action_generate_plan()
        return plan_id

    def button_open_budget_plan(self):
        self.ensure_one()
        return {
            "name": _("Budget Plan"),
            "type": "ir.actions.act_window",
            "res_model": "budget.plan",
            "view_mode": "form",
            "res_id": self.plan_id.id,
            "context": self.env.context,
        }
