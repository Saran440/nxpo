# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class FundConstraint(models.Model):
    _inherit = "fund.constraint"

    program_id = fields.Many2one(
        comodel_name="res.program",
    )
    program_allocation_id = fields.Many2one(
        comodel_name="res.program.allocation",
        ondelete="cascade",
    )
