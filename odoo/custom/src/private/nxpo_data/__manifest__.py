# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "NxPO - Migration Data",
    "summary": "Migration data, i.e., products, partners, projects, etc. "
    "**This module can be uninstalled afterwards**",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "NxPO",
    "author": "Ecosoft",
    "depends": ["base"],
    "data": [
        "data/res.users.csv",
        "data/res.project.csv",
        "data/budget.activity.group.csv",
        "data/budget.activity.csv",
        "data/mis.report.csv",
    ],
    "installable": True,
}
