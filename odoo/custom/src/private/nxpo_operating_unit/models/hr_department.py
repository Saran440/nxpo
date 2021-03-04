# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Department(models.Model):
    _inherit = "hr.department"

    operating_unit_id = fields.Many2one(
        comodel_name="operating.unit",
        string="Operating Unit",
        index=True,
        ondelete="restrict",
    )
    assist_deputy_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Assist Deputy",
        index=True,
        ondelete="restrict",
    )
