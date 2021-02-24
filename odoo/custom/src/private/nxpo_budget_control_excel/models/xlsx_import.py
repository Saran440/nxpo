# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

# import numpy as np
# import pandas as pd
# from openpyxl.utils.dataframe import dataframe_to_rows

from odoo import api, models


class XLSXImport(models.AbstractModel):
    _inherit = "xlsx.import"

    @api.model
    def import_xlsx(self, import_file, template, res_model=False, res_id=False):
        """Manipulate data from BudgetControl into RawData sheet,
        in the way it can be easily consumed by excel_import_export"""
        # print(
        #     "-------------------------------------"
        # )
        # print(import_file)
        # print(
        #     "======================================"
        # )
        record = super().import_xlsx(
            import_file, template, res_model=res_model, res_id=res_id
        )
        return record
