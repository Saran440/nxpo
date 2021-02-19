# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "NxPO Requests Activity",
    "version": "14.0.1.0.0",
    "category": "NxPO",
    "license": "AGPL-3",
    "author": "Ecosoft",
    "depends": [
        "budget_activity",
        "requests",
        "requests_hr_expense",
        "requests_purchase_request",
        # "nxpo_request_advance_line",
    ],
    "data": [
        "views/request_product_line_views.xml",
    ],
    "installable": True,
    "auto_install": True,
    "maintainers": ["kittiu"],
    "development_status": "Alpha",
}
