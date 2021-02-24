# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class BudgetControl(models.Model):
    _inherit = "budget.control"

    kpi_ids = fields.One2many(
        comodel_name="mis.report.kpi",
        related="budget_id.report_id.kpi_ids",
        help="Used to povide list of KPIs in excel sheet",
    )
