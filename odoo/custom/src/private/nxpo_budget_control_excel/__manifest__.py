# Copyright 2017-19 ForgeFlow S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "NxPO - Excel for Budget Control Sheet",
    "summary": "Import/Export Excel for Budget Control Sheet",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "NxPO",
    "depends": ["excel_import_export", "budget_control", "base_name_search_improved"],
    "external_dependencies": {"python": ["pandas", "numpy", "openpyxl"]},
    "data": [
        "views/actions.xml",
        "templates/templates.xml",
    ],
    "installable": True,
}
