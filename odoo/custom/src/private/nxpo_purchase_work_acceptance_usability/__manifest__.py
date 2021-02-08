# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "NxPO - Purchase Work Acceptance Usability",
    "summary": "Usability improvements on purchase module",
    "version": "14.0.1.0.0",
    "category": "NxPO",
    "author": "ProThai Technology Co.,Ltd.",
    "depends": [
        "purchase_work_acceptance",
        "purchase_work_acceptance_invoice_plan",
    ],
    "data": [
        "views/purchase_views.xml",
        "views/work_acceptance_view.xml",
    ],
    "installable": True,
    "license": "AGPL-3",
}
