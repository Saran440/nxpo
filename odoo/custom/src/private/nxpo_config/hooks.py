# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import datetime

from dateutil.rrule import MONTHLY

from odoo import SUPERUSER_ID, api


def delete_old_data(cr, registry):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        # Generate date range
        date_type_period = env["date.range.type"].search([("name", "=", "Period")])
        date_type_year = env["date.range.type"].search([("name", "=", "Year")])
        if not date_type_period:
            year = datetime.datetime.now().year
            start_year = 2020
            number_year = (year - start_year) + 2  # create 2020 to next current year
            date_type_period = env["date.range.type"].create(
                {"name": "Period", "company_id": 1, "allow_overlap": False}
            )
            for y in range(number_year):
                current_year = start_year + y
                generator = env["date.range.generator"].create(
                    {
                        "date_start": "%s-01-01" % (current_year),
                        "name_prefix": "%s/" % (current_year),
                        "type_id": date_type_period.id,
                        "duration_count": 1,
                        "unit_of_time": str(MONTHLY),
                        "count": 12,
                    }
                )
                generator.action_apply()
        if not date_type_year:
            date_type_period = env["date.range.type"].create(
                {"name": "Year", "company_id": 1, "allow_overlap": False}
            )
        # Archive demo data
        env.ref("hr.dep_administration").write({"active": False})
        env.ref("hr.dep_sales").write({"active": False})
        env.ref("operating_unit.main_operating_unit").write({"active": False})
