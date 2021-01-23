# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Inventory(models.Model):
    _inherit = "stock.inventory"

    note = fields.Text("Notes")
