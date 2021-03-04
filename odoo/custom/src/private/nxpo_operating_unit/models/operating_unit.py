# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class OperatingUnit(models.Model):
    _inherit = "operating.unit"

    manager_id = fields.Many2one(
        comodel_name="hr.employee", string="Deputy", index=True, ondelete="restrict"
    )
    department_ids = fields.One2many(
        comodel_name="hr.department",
        inverse_name="operating_unit_id",
        string="Departments",
    )
    assist_deputy_ids = fields.Many2many(
        comodel_name="hr.employee",
        string="Assist Deputy",
        compute="_compute_assist_deputy_ids",
    )

    @api.depends("department_ids")
    def _compute_assist_deputy_ids(self):
        for obj in self:
            obj.assist_deputy_ids = obj.department_ids.mapped("assist_deputy_id")
