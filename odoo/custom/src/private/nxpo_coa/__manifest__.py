# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "NxPO - Accounting",
    "version": "14.0.1.0.0",
    "category": "NxPO",
    "summary": "Chart of Accounts for NxPO.",
    "author": "Ecosoft",
    "website": "http://ecosoft.co.th/",
    "depends": ["account"],
    "license": "LGPL-3",
    "data": [
        "data/account_data.xml",
        "data/nxpo_chart_data.xml",
        "data/account.account.template.csv",
        "data/account_tax_report_data.xml",
        "data/account_tax_template_data.xml",
        "data/account_chart_template_data.xml",
    ],
    "post_init_hook": "post_init_hook",
}
