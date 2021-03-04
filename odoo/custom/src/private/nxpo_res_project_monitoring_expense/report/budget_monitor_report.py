# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class BudgetMonitorReport(models.Model):
    _inherit = "budget.monitor.report"

    # Expense
    def _select_ex_commit(self):
        select_ex_query = super()._select_ex_commit()
        select_ex_query.append("aa.project_id, rp.parent_project")
        return select_ex_query

    def _from_ex_commit(self):
        from_ex_query = super()._from_ex_commit()
        from_ex_query = "\n".join(
            [
                from_ex_query,
                "join account_analytic_account aa on \
                    a.analytic_account_id = aa.id \
                left outer join res_project rp on aa.project_id = rp.id",
            ]
        )
        return from_ex_query
