# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProcurementCommitteeLines(models.Model):
    _name = "procurement.committee.lines"
    _description = "Procurement Committees"

    employee_id = fields.Many2one(
        "hr.employee",
        string="Employee",
        required=True,
        ondelete="cascade",
    )
    name = fields.Char(related="employee_id.name")
    department_id = fields.Many2one(related="employee_id.department_id", readonly=True)
    email = fields.Char(related="employee_id.work_email", readonly=True)
    phone = fields.Char(related="employee_id.work_phone", readonly=True)
    committee_type = fields.Selection(
        [
            ("procurement", "Procurement Committee"),
            ("audit", "Audit Committee"),
        ],
        string="Committee Type",
        default=lambda self: self._context.get("committee_type", False),
    )
    request_id = fields.Many2one(
        comodel_name="purchase.request",
        string="Purchase Request",
        ondelete="cascade",
        readonly=True,
        index=True,
        auto_join=True,
    )
    approve_role = fields.Selection(
        [
            ("chief_committee", "Chief Committee"),
            ("audit_committee", "Audit Committee"),
        ],
        string="Role",
        default=lambda self: self._context.get("default_approve_role", False),
        required=True,
    )
    state = fields.Selection(
        [
            ("active", "Active"),
            ("cancel", "Cancelled"),
        ],
        string="Status",
        required=True,
        default="active",
    )
    note = fields.Text("Note")

    _sql_constraints = [
        (
            "employee_request_uniq",
            "unique (employee_id,request_id)",
            "The employee must be unique per purchase pequest !",
        )
    ]

    @api.onchange("employee_id")
    def onchange_employee_id(self):
        if self.employee_id:
            self.name = self.employee_id.name
