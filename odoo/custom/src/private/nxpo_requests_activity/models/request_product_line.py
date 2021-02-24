# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class RequestProductLine(models.Model):
    _inherit = "request.product.line"

    activity_id = fields.Many2one(
        comodel_name="budget.activity",
        string="Activity",
        readonly=False,
    )