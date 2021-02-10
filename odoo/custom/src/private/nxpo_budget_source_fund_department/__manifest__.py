# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "NxPO - Add department on Budget Source of Funds",
    "summary": "Add fields department on budget source of fund for NxPO",
    "version": "14.0.1.0.0",
    "category": "NxPO",
    "license": "AGPL-3",
    "author": "Ecosoft",
    "depends": ["budget_source_fund", "nxpo_budget_control_department"],
    "data": [
        "views/budget_source_fund_line_view.xml",
        "views/budget_source_fund_view.xml",
    ],
    "installable": True,
    "maintainers": ["Saran440"],
    "development_status": "Alpha",
}
