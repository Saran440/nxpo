# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from ast import literal_eval

from odoo import models


class StockRequestOrder(models.Model):
    _inherit = "stock.request.order"

    def action_view_stock_valuation_layers(self):
        self.ensure_one()
        scraps = self.env["stock.scrap"].search(
            [("picking_id", "in", self.picking_ids.ids)]
        )
        move_lines = self.env["stock.move"].search(
            [("picking_id", "in", self.picking_ids.ids)]
        )
        domain = [
            ("id", "in", (move_lines + scraps.move_id).stock_valuation_layer_ids.ids)
        ]
        action = self.env["ir.actions.actions"]._for_xml_id(
            "stock_account.stock_valuation_layer_action"
        )
        context = literal_eval(action["context"])
        context.update(self.env.context)
        context["no_at_date"] = True
        return dict(action, domain=domain, context=context)
