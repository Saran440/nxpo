# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    procurement_type_id = fields.Many2one(
        comodel_name="procurement.type",
        string="Procurement Type",
        ondelete="restrict",
    )
