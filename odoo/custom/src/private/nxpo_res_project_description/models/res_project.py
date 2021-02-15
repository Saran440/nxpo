# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResProject(models.Model):
    _inherit = "res.project"

    description = fields.Html(
        readonly=True, copy=False, states={"draft": [("readonly", False)]}
    )
