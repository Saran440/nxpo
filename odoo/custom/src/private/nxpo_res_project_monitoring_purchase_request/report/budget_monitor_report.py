# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class BudgetMonitorReport(models.Model):
    _inherit = "budget.monitor.report"

    # Purchase
    def _select_pr_commit(self):
        select_pr_query = super()._select_pr_commit()
        select_pr_query.append("aa.project_id, rp.parent_project")
        return select_pr_query

    def _from_pr_commit(self):
        from_pr_query = super()._from_pr_commit()
        from_pr_query = "\n".join(
            [
                from_pr_query,
                "join account_analytic_account aa on \
                    a.analytic_account_id = aa.id \
                left outer join res_project rp on aa.project_id = rp.id",
            ]
        )
        return from_pr_query
