# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"

    default_approve_role = fields.Char(compute="_compute_approve_role")
    committee_procurement_line_ids = fields.One2many(
        comodel_name="procurement.committee.lines",
        inverse_name="request_id",
        string="Procurement Committees",
        domain=[("committee_type", "=", "procurement")],
        copy=True,
    )
    committee_audit_line_ids = fields.One2many(
        comodel_name="procurement.committee.lines",
        inverse_name="request_id",
        string="Audit Committees",
        domain=[("committee_type", "=", "audit")],
        copy=True,
    )

    @api.depends("committee_audit_line_ids")
    def _compute_approve_role(self):
        for obj in self:
            default_approve_role = [
                com.approve_role
                for com in obj.committee_audit_line_ids
                if com.approve_role == "chief_committee"
            ]
            if default_approve_role:
                obj.default_approve_role = "audit_committee"
            else:
                obj.default_approve_role = "chief_committee"

    def _check_committee_lines(self):
        check_committee_lines = self.committee_audit_line_ids.filtered(
            lambda c: c.approve_role == "chief_committee"
        )
        if not check_committee_lines:
            raise UserError(
                _(
                    "Must have an committee, "
                    "At least 1 person who is the chief committee."
                )
            )
        return True

    def request_validation(self):
        self._check_committee_lines()
        return super().request_validation()
