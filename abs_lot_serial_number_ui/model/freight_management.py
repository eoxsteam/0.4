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

class FreightManagement(models.Model):
    _inherit = 'freight.management'

    def create(self, vals):
        res= super(FreightManagement, self).create(vals)
        self.udpate_shipping_fields_lot_serial_number()
        return res

    def write(self, vals):
        res= super(FreightManagement, self).write(vals)
        self.udpate_shipping_fields_lot_serial_number()
        return res

    def udpate_shipping_fields_lot_serial_number(self):
        lot_serial_id = self.env['stock.production.lot'].search([('po_number','=',self.purchase_order_id.name)])
        if lot_serial_id:
            for lot_serial in lot_serial_id:
                for rec in self.frm_line_ids:
                    lot_serial.update({'ship_from_id': rec.source_location.id,
                                       'ship_to_id': rec.dest_location.id,
                                       'ship_via_id': rec.mode_id.id,
                                       'purchase_incoterm_id': self.purchase_order_id.incoterm_id.id
                                     })
