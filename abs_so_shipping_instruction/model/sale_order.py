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

from odoo import api, models, fields,_

class SaleOrder(models.Model):
    _inherit = "sale.order"

    ship_via_id = fields.Many2one("frm.mode.operation",string="Ship Via")
    expected_delivery_date = fields.Date(string="Expected Delivery Date")
    max_bundle_weight = fields.Integer(string="Max. Bundle Weight")
    fob = fields.Char(string="FOB")
    si_warehouse_id = fields.Many2one("stock.warehouse",string="Shipping Warehouse") 
    customer_id = fields.Many2one("res.partner",string="Shipping Customer")
    res_address_id = fields.Many2one("res.partner",string="Address")

    @api.onchange('partner_id')
    def onchange_partner_id_shipping_instuction(self):
        result = super(SaleOrder, self).onchange_partner_id()
        values = {}
        if self.partner_id:
            values['customer_id'] = self.partner_id.id
            delivery_address = self.partner_id.address_get(['delivery'])
            values['res_address_id'] = delivery_address['delivery']
        else:
            values['customer_id'] = False
            values['res_address_id'] = False
        if values:
            self.update(values)
        return result
        
    @api.onchange('partner_shipping_id')
    def onchange_partner_shipping_id_delivery_address(self):
        result = super(SaleOrder, self).onchange_partner_shipping_id()
        if self.partner_shipping_id:
            self.res_address_id = self.partner_shipping_id.id
        else:
            self.res_address_id = False
        return result
