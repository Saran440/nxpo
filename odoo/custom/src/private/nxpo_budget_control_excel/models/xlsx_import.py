# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

import base64
from io import BytesIO

import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

from odoo import _, api, models
from odoo.exceptions import ValidationError


class XLSXImport(models.AbstractModel):
    _inherit = "xlsx.import"

    @api.model
    def import_xlsx(self, import_file, template, res_model=False, res_id=False):
        if self._context.get("is_budget_control_sheet"):
            import_file = self._transform_budget_control_sheet(import_file)
        record = super().import_xlsx(
            import_file, template, res_model=res_model, res_id=res_id
        )
        return record

    def _transform_budget_control_sheet(self, import_file):
        # Get the budget control sheet
        res_id = self._context["active_id"]
        budget_control = self.env["budget.control"].browse(res_id)
        # Read excel from sheet "BudgetControl" as data frame
        content = BytesIO(base64.decodebytes(import_file))
        df = pd.read_excel(content, sheet_name="BudgetControl", header=None)
        matrix_df = df.iloc[8:, :13]  # Get only matrix from cell A9 to column M
        # Expand the matrix into mis.budget.item table
        # [kpi, period, amount, budget_id, date_from, date_to, anlaytic]
        rows = dataframe_to_rows(matrix_df, index=False, header=False)
        rows = [x for x in rows if x != [0]]
        periods = self.env["date.range"].search(
            [
                ("date_start", ">=", budget_control.date_from),
                ("date_end", "<=", budget_control.date_to),
            ],
            order="date_start",
        )
        if len(periods) != 12:
            raise ValidationError(_("Cannot setup 12 periods for budget control"))
        budget_items = []
        for r in rows:
            kpi = r[0]
            ag = kpi.strip()
            # Get the description part, i.e., "AG1 (ag1)" -> "AG1"
            if ag.endswith(")") and "(" in ag:
                ag = ag[: ag.rfind("(")].strip()
            for m in range(0, 12):
                budget_items.append(
                    [
                        ag,
                        periods[m].name,
                        r[m + 1],
                        self.get_external_id(budget_control.budget_id),
                        periods[m].date_start,
                        periods[m].date_end,
                        self.get_external_id(budget_control.analytic_account_id),
                    ]
                )
        # Create data frame from mis.budget.item data table, and return as new excel
        result_df = pd.DataFrame(budget_items)
        # Ensure amount is summed for the same keys
        result_df = result_df.groupby([0, 1, 3, 4, 5, 6])[[2]].sum()
        result_df = result_df.reset_index().sort_index(axis=1)
        new_content = BytesIO()
        result_df.to_excel(
            new_content, sheet_name="ImportData", index=False, header=False
        )
        new_content.seek(0)  # Set index to 0, and start reading
        new_file = base64.encodebytes(new_content.read())
        return new_file
