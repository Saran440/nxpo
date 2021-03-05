# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class BaseDisplayName(models.AbstractModel):
    _inherit = "base.display.name"

    def _get_display(self, field_display):
        field_code = ""
        if field_display[0]:
            field_code = "[{}]".format(field_display[0])
        return " ".join([field_code, field_display[1]])
