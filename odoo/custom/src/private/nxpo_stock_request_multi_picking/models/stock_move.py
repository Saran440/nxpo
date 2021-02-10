# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _split(self, qty, restrict_partner_id=False):
        new_move_vals = super()._split(qty, restrict_partner_id)
        for al in self.allocation_ids:
            qty = al.requested_product_uom_qty - self.quantity_done
            new_move_vals[0].update(
                {
                    "allocation_ids": [
                        (
                            0,
                            0,
                            {
                                "stock_request_id": al.stock_request_id.id,
                                "requested_product_uom_qty": qty,
                            },
                        )
                    ]
                }
            )
            al.update({"requested_product_uom_qty": self.quantity_done})
        return new_move_vals
