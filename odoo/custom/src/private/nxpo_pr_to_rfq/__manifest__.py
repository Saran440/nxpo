# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "NxPO - Purchase Request to RFQ",
    "summary": "Create RFQ from selected purchase request",
    "version": "14.0.1.0.0",
    "category": "NxPO",
    "author": "ProThai Technology Co.,Ltd.",
    "depends": ["nxpo_purchase_usability"],
    "data": [
        # wizards
        "wizards/purchase_request_line_make_purchase_order_view.xml",
    ],
    "installable": True,
    "license": "AGPL-3",
}
