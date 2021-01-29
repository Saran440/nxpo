# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "NxPO - Purchase Usability",
    "summary": "Usability improvements on purchase module",
    "version": "14.0.1.0.0",
    "category": "NxPO",
    "author": "ProThai Technology Co.,Ltd.",
    "depends": [
        "purchase",
        "purchase_request",
        "purchase_order_type",
        "purchase_request_type",
        "nxpo_base_usability",
    ],
    "data": [
        "views/action_hidden_views.xml",
        "views/purchase_views.xml",
        "views/purchase_order_type_view.xml",
        "views/purchase_request_type_view.xml",
    ],
    "installable": True,
    "license": "AGPL-3",
}
