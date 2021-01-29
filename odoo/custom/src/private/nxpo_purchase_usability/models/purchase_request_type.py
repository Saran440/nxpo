# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class PurchaseRequestType(models.Model):
    _inherit = "purchase.request.type"

    code = fields.Char(
        string="Code",
    )

    @api.depends("name", "code")
    def name_get(self):
        result = []
        for pr in self:
            name = pr.name
            if pr.code:
                name = "[%s] %s" % (pr.code, name)
            result.append((pr.id, name))
        return result
