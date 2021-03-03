# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    director_id = fields.Many2one(
        comodel_name="hr.employee", string="Director", index=True, ondelete="restrict"
    )
