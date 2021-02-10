# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProcurementType(models.Model):
    _name = "procurement.type"
    _description = "Procurement Type"
    _order = "sequence"

    name = fields.Char(required=True)
    code = fields.Char(string="Code")
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)
    description = fields.Text(string="Description", translate=True)

    def name_get(self):
        result = []
        for pc in self:
            name = pc.name
            if pc.code:
                name = "[%s] %s" % (pc.code, name)
            result.append((pc.id, name))
        return result
