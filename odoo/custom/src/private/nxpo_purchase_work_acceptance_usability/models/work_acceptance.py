# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorkAcceptanceLine(models.Model):
    _inherit = "work.acceptance.line"

    installment_id = fields.Many2one(related="wa_id.installment_id")
