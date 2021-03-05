# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ResProgram(models.Model):
    _inherit = "res.program"
    _name = "res.program"
    _inherit = ["res.program", "base.display.name"]
    _description = "Program display code"
    _field_display = ["code", "name"]
