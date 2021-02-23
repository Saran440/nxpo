# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "NxPO - Install",
    "summary": "Listing of all required module for easy installation. "
    "**This module can be uninstalled afterwards**",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "NxPO",
    "author": "Ecosoft",
    "depends": [
        # Odoo Modules
        "mail",
        "purchase",
        "account",
        "hr_expense",
        # OCA Modules
        "base_rest",  # this will be standard webservice for this project
        "date_range",
        "account_menu",
        "account_financial_report",
        "purchase_request",
        "account_asset_management",
        "analytic_base_department",
        "operating_unit",
        "analytic_operating_unit",
        "account_operating_unit",
        "hr_expense_sequence",
        "hr_expense_operating_unit",
        "hr_expense_advance_clearing_detail",
        "purchase_operating_unit",
        "purchase_request_operating_unit",
        "l10n_th_base_location",
        "mis_builder_budget_activity_group",
        "base_tier_validation_formula",
        "base_tier_validation_forward",
        "base_tier_validation_server_action",
        "budget_control",
        "budget_control_selection_plan",
        "budget_control_expense",
        "budget_control_purchase",
        "budget_control_purchase_request",
        "budget_control_advance_clearing",
        "budget_control_revision",
        "budget_control_revision_plan_readonly",
        "budget_control_revision_department_monitoring",
        "budget_control_transfer",
        "budget_control_transfer_operating_unit",
        "budget_control_transfer_tier_validation",
        "budget_control_exception",
        "budget_control_operating_unit",
        "budget_source_fund",
        "budget_source_fund_group",
        "budget_source_fund_objective",
        "budget_plan",
        "budget_plan_fund_constraint",
        "budget_plan_revision",
        # "budget_source_fund_operating_unit", # May be this module is not used.
        "budget_activity",
        "budget_activity_group",
        "budget_activity_monitoring",
        "budget_activity_monitoring_purchase_request",
        # "budget_monitoring_operating_unit",
        "fund_constraint",
        "fund_constraint_actual",
        # NxPO Modules
        "nxpo_budget_control_department",
        # "nxpo_budget_source_fund_department", # May be this module is not used.
        "nxpo_res_project",
        "nxpo_res_project_description",
        "nxpo_res_project_analytic",
        "nxpo_res_project_department",
        "nxpo_res_project_member",
        "nxpo_res_project_monitoring_report",
        "nxpo_budget_invisible",
        "nxpo_budget_transfer_department",
        "nxpo_budget_revision_monitoring_project",
        "nxpo_advance_clearing_detail_analytic",
    ],
    "installable": True,
}
