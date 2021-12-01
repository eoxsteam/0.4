# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2021-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from odoo import models, fields, api, _

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def stock_lot_action(self):
        return {
            "name": _("Add Product Detail"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "stock.production.lot",
            "res_id": self.lot_id.id,
            "views": [(False, "form")],
            "view_id": "stock.view_production_lot_form",
            "target": "new",
            # 'context': ctx,
        }
