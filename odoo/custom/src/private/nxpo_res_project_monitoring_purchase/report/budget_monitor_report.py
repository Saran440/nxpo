# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class BudgetMonitorReport(models.Model):
    _inherit = "budget.monitor.report"

    # Purchase
    def _select_po_commit(self):
        select_po_query = super()._select_po_commit()
        select_po_query.append("aa.project_id, rp.parent_project")
        return select_po_query

    def _from_po_commit(self):
        from_po_query = super()._from_po_commit()
        from_po_query = "\n".join(
            [
                from_po_query,
                "join account_analytic_account aa on \
                    a.analytic_account_id = aa.id \
                left outer join res_project rp on aa.project_id = rp.id",
            ]
        )
        return from_po_query
