# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class BudgetMonitorReport(models.Model):
    _inherit = "budget.monitor.report"

    # Purchase
    def _select_av_commit(self):
        select_av_query = super()._select_av_commit()
        select_av_query.append("aa.project_id, rp.parent_project")
        return select_av_query

    def _from_av_commit(self):
        from_av_query = super()._from_av_commit()
        from_av_query = "\n".join(
            [
                from_av_query,
                "join account_analytic_account aa on \
                    a.analytic_account_id = aa.id \
                left outer join res_project rp on aa.project_id = rp.id",
            ]
        )
        return from_av_query
