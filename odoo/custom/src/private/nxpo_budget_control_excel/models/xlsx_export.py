# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

import numpy as np
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

from odoo import api, models


class XLSXExport(models.AbstractModel):
    _inherit = "xlsx.export"

    @api.model
    def _fill_workbook_data(self, workbook, record, data_dict):
        """ Fill data processed from pandas after normal fill """
        super()._fill_workbook_data(workbook, record, data_dict)
        if self._context.get("is_budget_control_sheet"):
            self._fill_budget_control_sheet(workbook, data_dict)

    @api.model
    def _fill_budget_control_sheet(self, workbook, data_dict):
        raw_data = workbook["RawData"]
        budget_control = workbook["BudgetControl"]
        df = pd.DataFrame(raw_data.values)
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        # Make pivot_table
        table = pd.pivot_table(
            df, values=2, index=[0], columns=[1], aggfunc=np.sum, fill_value=0
        )
        pos = (1, 9)  # Will paste the pivot toable to cell A9
        rows = dataframe_to_rows(table, index=True, header=False)
        rows = [x for x in rows if x != [0]]  # from generator to array, no header
        for r_idx, row in enumerate(rows, pos[1]):
            for c_idx, value in enumerate(row, pos[0]):
                budget_control.cell(row=r_idx, column=c_idx, value=value)
            # Sum at the end of row
            budget_control.cell(row=r_idx, column=c_idx + 1, value="=SUM(B9:M9)")
