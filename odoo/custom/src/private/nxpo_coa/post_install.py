# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    from odoo.addons.account.models.chart_template import (
        preserve_existing_tags_on_taxes,
    )

    preserve_existing_tags_on_taxes(cr, registry, "nxpo_coa")
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        chart_template = env["account.chart.template"]
        coa = chart_template.search([("name", "=", "NxPO - Chart of Accounts")])
        a_recv = env.ref("nxpo_coa.a_recv")
        a_pay = env.ref("nxpo_coa.a_pay")
        a_exp_cogs = env.ref("nxpo_coa.a_exp_cogs")
        a_sales = env.ref("nxpo_coa.a_sales")
        a_income_gain = env.ref("nxpo_coa.a_income_gain")
        a_exp_loss = env.ref("nxpo_coa.a_exp_loss")
        coa.property_account_receivable_id = a_recv
        coa.property_account_payable_id = a_pay
        coa.property_account_expense_categ_id = a_exp_cogs
        coa.property_account_income_categ_id = a_sales
        coa.income_currency_exchange_account_id = a_income_gain
        coa.expense_currency_exchange_account_id = a_exp_loss
        # Uninstall and loading coa template again
        env.company.chart_template_id = False
        coa.try_loading()
    return
