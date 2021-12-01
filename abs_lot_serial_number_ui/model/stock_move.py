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
    _inherit = 'stock.move.line'

    def get_lot_serial(self):
        res = super(StockMoveLine,self).get_lot_serial()
        lot_id = self.env['stock.production.lot'].search([('id','=',res['res_id'])])
        purchase_order_id = self.env['purchase.order'].search([('name','=',self.origin)])
        if lot_id:
            for rec in purchase_order_id.order_line:
                if rec.product_id.id == self.product_id.id:
                    lot_id.update({'unit_cost': rec.price_unit,
                                 })
            lot_id.update({'date_received':self.picking_id.scheduled_date,
                           'purchase_cose_untexed':purchase_order_id.amount_untaxed,
                           'purchase_cose_texed':purchase_order_id.amount_total,
                           'vendor_location_id' : purchase_order_id.partner_id.id
                         })
        return res
