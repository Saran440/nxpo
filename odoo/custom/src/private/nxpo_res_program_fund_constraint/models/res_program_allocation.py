# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


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
