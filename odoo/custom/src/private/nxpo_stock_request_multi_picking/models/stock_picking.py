# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def check_stock_request_cancel(self):
        """
        1. Check multiple stock picking status to cancel items
        2. Check done stock request when the picking status is not canceled
        """

        pickings = self.stock_request_ids.mapped("move_ids.picking_id").filtered(
            lambda p: p.state != "cancel"
        )
        # 1
        if not pickings and self.stock_request_ids.mapped("move_ids.picking_id"):
            for request in self.stock_request_ids:
                request.order_id.action_cancel()
        else:
            # 2
            for request in self.stock_request_ids:
                request.check_done()
        return True

    def action_cancel(self):
        res = super().action_cancel()
        self.check_stock_request_cancel()
        return res
