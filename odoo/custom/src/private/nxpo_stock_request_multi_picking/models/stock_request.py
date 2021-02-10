# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models
from odoo.tools import float_compare


class StockRequest(models.Model):
    _inherit = "stock.request"

    def check_done(self):
        for request in self:
            # check qty stock move status cancel
            allocated_move_cancel = request.allocation_ids.filtered(
                lambda al: al.allocated_product_qty == 0
                and al.stock_move_id.state == "cancel"
            )

            if allocated_move_cancel:
                precision = self.env["decimal.precision"].precision_get(
                    "Product Unit of Measure"
                )
                allocated_qty = sum(
                    request.allocation_ids.mapped("allocated_product_qty")
                ) + sum(allocated_move_cancel.mapped("stock_move_id.product_uom_qty"))
                qty_done = request.product_id.uom_id._compute_quantity(
                    allocated_qty, request.product_uom_id
                )
                if (
                    float_compare(
                        qty_done, request.product_uom_qty, precision_digits=precision
                    )
                    >= 0
                ):
                    request.action_done()
            else:
                super().check_done()
        return True
