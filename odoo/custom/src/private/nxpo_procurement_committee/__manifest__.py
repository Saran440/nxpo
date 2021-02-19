# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "NxPO - Procurement Committee",
    "summary": "Add tab procurement committee to purchase request",
    "version": "14.0.1.0.0",
    "category": "NxPO",
    "author": "ProThai Technology Co.,Ltd.",
    "depends": ["hr", "purchase_request", "purchase_request_tier_validation"],
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_request_view.xml",
    ],
    "maintainer": ["prapassornS"],
    "installable": True,
    "license": "AGPL-3",
}
