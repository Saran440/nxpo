# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResProgram(models.Model):
    _name = "res.program"
    _description = "Program"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
