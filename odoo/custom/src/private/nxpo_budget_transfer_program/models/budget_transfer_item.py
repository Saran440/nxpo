# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class BudgetTransferItem(models.Model):
    _inherit = "budget.transfer.item"

    target_program_id = fields.Many2one(
        comodel_name="res.program",
        string="Destination Program",
        compute="_compute_program_id",
        store="True",
        readonly=False,
        required=True,
    )
    target_program_all = fields.Many2many(
        comodel_name="res.program",
        relation="target_transfer_program_rel",
        column1="transfer_id",
        column2="target_program_id",
        compute="_compute_program_all",
        compute_sudo=True,
    )
    source_program_id = fields.Many2one(
        comodel_name="res.program",
        compute="_compute_program_id",
        store="True",
        readonly=False,
        required=True,
    )
    source_program_all = fields.Many2many(
        comodel_name="res.program",
        relation="source_transfer_program_rel",
        column1="transfer_id",
        column2="source_program_id",
        compute="_compute_program_all",
        compute_sudo=True,
    )

    def _get_program(self, budget_control):
        program = budget_control.fund_constraint.mapped("program_id")
        return program

    @api.depends("target_budget_control_id", "source_budget_control_id")
    def _compute_program_id(self):
        for rec in self:
            target_program = rec._get_program(rec.target_budget_control_id)
            source_program = rec._get_program(rec.source_budget_control_id)
            rec.target_program_id = (
                len(target_program) == 1 and target_program.id or False
            )
            rec.source_program_id = (
                len(source_program) == 1 and source_program.id or False
            )

    @api.depends("target_budget_control_id", "source_budget_control_id")
    def _compute_program_all(self):
        for rec in self:
            rec.target_program_all = rec._get_program(rec.target_budget_control_id)
            rec.source_program_all = rec._get_program(rec.source_budget_control_id)

    def _check_fund_constraint(self):
        if any(rec.target_program_id != rec.source_program_id for rec in self):
            raise UserError(_("Must be the same program."))
