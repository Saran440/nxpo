# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "NxPO - Procurement Type",
    "version": "14.0.1.0.0",
    "category": "NxPO",
    "author": "ProThai Technology Co.,Ltd.",
    "depends": ["purchase_request_type"],
    "data": [
        "security/ir.model.access.csv",
        "data/procurement_type.xml",
        # views
        "views/procurement_type_view.xml",
        "views/purchase_request_view.xml",
        "views/purchase_view.xml",
        "views/purchase_request_type_view.xml",
        # wizards
        "wizards/purchase_request_line_make_purchase_order_view.xml",
    ],
    "installable": True,
    "license": "AGPL-3",
}
