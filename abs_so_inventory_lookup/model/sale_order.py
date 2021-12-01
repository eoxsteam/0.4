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

    def button_inventory_lookup_by_item(self):
        return {
                "name": _("By Item Info"),
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model":"by.item.info.wizard",
                "views":[(False,"form")],
                "view_id":self.env.ref("abs_inventory_lookup.view_by_item_info_form",
                                       "False"),
                "target":"new",
                "binding_view_types":"form"
               }
 
    def button_inventory_lookup_by_chemistries(self):
         return {
                "name": _("By Chemistries"),
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model":"by.chemistries.wizard",
                "views":[(False,"form")],
                "view_id":self.env.ref("abs_inventory_lookup.view_by_chemistries_form",
                                       "False"),
                "target":"new",
                "binding_view_types":"form"
               }
