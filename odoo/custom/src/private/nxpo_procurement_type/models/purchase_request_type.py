# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class PurchaseRequestType(models.Model):
    _inherit = "purchase.request.type"

    procurement_type_ids = fields.Many2many(
        comodel_name="procurement.type",
        string="Allowed Procurement Type",
    )
