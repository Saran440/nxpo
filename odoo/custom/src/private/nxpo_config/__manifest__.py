# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "NxPO - Configuration Data",
    "summary": "Configuration data, to be loaded after nxpo_install"
    "**This module can be uninstalled afterwards**",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "NxPO",
    "author": "Ecosoft",
    "depends": [
        "base",
    ],
    "data": [
        "data/res_partner_data.xml",
        "data/operating.unit.csv",
        "data/operating_unit_data.xml",
        "data/hr.department.csv",
    ],
    "installable": True,
    "post_init_hook": "delete_old_data",
}
