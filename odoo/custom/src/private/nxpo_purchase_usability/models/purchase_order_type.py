# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class PurchaseOrderType(models.Model):
    _inherit = "purchase.order.type"

    code = fields.Char("Code")
    to_contract = fields.Boolean(string="Contract", default=False)

    @api.depends("name", "code")
    def name_get(self):
        result = []
        for po in self:
            name = po.name
            if po.code:
                name = "[%s] %s" % (po.code, name)
            result.append((po.id, name))
        return result
