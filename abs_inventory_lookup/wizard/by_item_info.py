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
from odoo import api, fields, models, _

class ByItemInfoWizard(models.TransientModel):
    _name = "by.item.info.wizard"
    _description = "By Item Info Wizard"

    info_category_id = fields.Many2one("product.category",
                                       string="Master",domain="[('parent_id', '=', False)]")
    info_sub_category_id = fields.Many2one("product.category",
                                           string="Sub Category", domain="[('parent_id', '!=', False)]")
    info_sub_product_id = fields.Many2one("product.product",
                                          string="Sub Product")
    info_partner_id = fields.Many2one("res.partner",
                                      string="Vendor")
    info_partner_no_id = fields.Char(string="Vendor No",
                                    related="info_partner_id.vendor_serial_number")
    info_partner_reserver_id = fields.Many2one("res.partner",
                                               string="Reserve Customer")
    # info_gauge_min = fields.Integer(string="Gauge(Min-Max)")
    # info_gauge_max = fields.Integer(string="Gauge-Max")
    info_gauge_min = fields.Many2many('steel.gauge', string="Thickness(Min-Max)")
    info_thickness_min = fields.Float(string="Thickness(Min-Max)")
    info_thickness_max = fields.Float(string="Thickness-Max")
    info_width_min = fields.Float(string="Width(Min-Max)")
    info_width_max = fields.Float(string="Width-Max")
    info_width_selection = fields.Selection([("mm","MM"),
                                            ("in","IN")],
                                            string="MM/IN",
                                             default="mm")
    info_length_min = fields.Float(string="Length(Min-Max)")
    info_length_max = fields.Float(string="Length-Max")
    info_len_selection = fields.Selection([("mm","MM"),
                                          ("in","IN")],
                                          string="Len MM/IN",
                                          default="mm")
    info_weight_min = fields.Integer(string="Weight(Min-Max)")
    info_weight_max = fields.Integer(string="Weight-Max")
    info_weight_selection = fields.Selection([("lbs","Lbs"),
                                     ("kg","KG")],
                                     string="LBS/KG",
                                     default="lbs")
    info_nct_id = fields.Many2one("res.nct.ct",
                                  string="NCT/CT")
    info_oil_id = fields.Many2one("res.oil.dry",
                                 string="Dry/Oil")
    info_id_gauge_min = fields.Integer(string="ID Gauge(Min-Max)")
    info_id_gauge_max = fields.Integer(string="ID Gauge-Max")
    info_od_gauge_min = fields.Integer(string="OD Gauge(Min-Max)")
    info_od_gauge_max = fields.Integer(string="OD Gauge-Max")
    info_piw_min = fields.Float(string="PIW(Min-Max)")
    info_piw_max = fields.Float(string="PIW-Max")
    info_yield_min = fields.Float(string="Yield(Min-Max)")
    info_yield_max = fields.Float(string="Yield-Max")
    info_yield_selection = fields.Selection([("mpa","MPA"),
                                            ("psi","PSI"),
                                            ("ksi","KSI")],
                                            string="MPS/PSI/KSI",
                                            default="mpa")
    info_tensile_min = fields.Float(string="Tensile(Min-Max)")
    info_tensile_max = fields.Float(string="Tensile-Max")
    info_tensile_selection = fields.Selection([("mpa","MPA"),
                                        ("psi","PSI"),
                                        ("ksi","KSI")],
                                        string="Tensile MPS/PSI/KSI",
                                        default="mpa")
    info_elongation_min = fields.Float(string="Elongation(Min-Max)")
    info_elongation_max = fields.Float(string="Elongation-Max")
    info_received = fields.Selection([("received","Received"),
                                     ("sold","Sold")],
                                     string="Received")
    info_start_date = fields.Date(string="Received Date")
    info_end_date = fields.Date(string="Sold Date")
    info_stock_status = fields.Selection([("transit","In Transit"),
                                         ("available","Available"),
                                         ("reserved","Reserved"),
                                         ("in_production","In production"),
                                         ("not_available","Not available")],
                                         string="Stock Status")

    @api.onchange('info_sub_category_id')
    def onchange_sub_category_id(self):
        for rec in self:
            return {'domain': {'info_sub_product_id': [('categ_id', '=', rec.info_sub_category_id.id)]}}

    def button_by_item_info_search(self):
        # print("\n\n\nbutton_by_item_info_search================",self)
        domain_list = []
        if self.info_category_id:
            domain_list.append(("category_id.id",
                                "=",
                                self.info_category_id.id))
        if self.info_sub_category_id:
            domain_list.append(("sub_category_id.id",
                                "=",
                                self.info_sub_category_id.id))
        if self.info_sub_product_id:
            domain_list.append(("product_id.id",
                                "=",
                                self.info_sub_product_id.id))
        if self.info_partner_reserver_id:
            domain_list.append(("reserve_customer_id.id",
                                "=",
                                self.info_partner_reserver_id.id))
        if self.info_partner_id:
            domain_list.append(("vendor_id.id",
                                "=",
                                self.info_partner_id.id))
        if self.info_nct_id:
            domain_list.append(("res_nct_ct_id.id",
                                "=",
                                self.info_nct_id.id))
        if self.info_oil_id:
            domain_list.append(("res_oil_dry_id.id",
                                "=",
                                self.info_oil_id.id))
        if self.info_stock_status:
            domain_list.append(("stock_status",
                                "=",
                                self.info_stock_status))
        if self.info_thickness_min and self.info_thickness_max:
            domain_list.append(("thickness_mm", ">=", self.info_thickness_min))
            domain_list.append(("thickness_mm", "<=", self.info_thickness_max))
        
        if self.info_width_min and self.info_width_max:
            if self.info_width_selection == "mm":
                domain_list.append(("width_mm", ">=", self.info_width_min))
                domain_list.append(("width_mm", "<=", self.info_width_max))
            else:
                domain_list.append(("width_in", ">=", self.info_width_min))
                domain_list.append(("width_in", "<=", self.info_width_max))

        if self.info_length_min and self.info_length_max:
            if self.info_len_selection == "mm":
                domain_list.append(("length_mm", ">=", self.info_length_min))
                domain_list.append(("length_mm", "<=", self.info_length_max))
            else:
                domain_list.append(("length_in", ">=", self.info_length_min))
                domain_list.append(("length_in", "<=", self.info_length_max))
      
        if self.info_weight_min and self.info_weight_max:
            if self.info_weight_selection == "lbs":
                domain_list.append(("weight_lb", ">=", self.info_weight_min))
                domain_list.append(("weight_lb", "<=", self.info_weight_max))
            else:
                # 1kg = 2.20462262185 lbs
                min_lbs = self.info_weight_min * 2.20462262185  
                max_lbs = self.info_weight_max * 2.20462262185
                domain_list.append(("weight_lb", ">=", min_lbs))
                domain_list.append(("weight_lb", "<=", max_lbs))
 
        """if self.info_piw_min and self.info_piw_max:
            domain_list.append(("piw", ">=", self.info_piw_min))
            domain_list.append(("piw", "<=", self.info_piw_max))"""

        if self.info_id_gauge_min and self.info_id_gauge_max:
            domain_list.append(("id_lot_stock", ">=", self.info_id_gauge_min))
            domain_list.append(("id_lot_stock", "<=", self.info_id_gauge_max))

        if self.info_od_gauge_min and self.info_od_gauge_max:
            domain_list.append(("lot_od", ">=", self.info_od_gauge_min))
            domain_list.append(("lot_od", "<=", self.info_od_gauge_max))

        if self.info_yield_min and self.info_yield_max:
            if self.info_yield_selection == "mpa":
                domain_list.append(("yield_mpa", ">=", self.info_yield_min))
                domain_list.append(("yield_mpa", "<=", self.info_yield_max))
            elif self.info_yield_selection == "psi":
                domain_list.append(("yield_psi", ">=", self.info_yield_min))
                domain_list.append(("yield_psi", "<=", self.info_yield_max))
            elif self.info_yield_selection == "ksi":
                domain_list.append(("yield_ksi", ">=", self.info_yield_min))
                domain_list.append(("yield_ksi", "<=", self.info_yield_max))

        if self.info_tensile_min and self.info_tensile_max:
            if self.info_tensile_selection == "mpa":
                domain_list.append(("tensile_mpa", ">=", self.info_tensile_min))
                domain_list.append(("tensile_mpa", "<=", self.info_tensile_max))
            elif self.info_tensile_selection == "psi":
                domain_list.append(("tensile_psi", ">=", self.info_tensile_min))
                domain_list.append(("tensile_psi", "<=", self.info_tensile_max))
            elif self.info_tensile_selection == "ksi":
                domain_list.append(("tensile_ksi", ">=", self.info_tensile_min))
                domain_list.append(("tensile_ksi", "<=", self.info_tensile_max))
         
        if self.info_elongation_min and self.info_elongation_max:
            domain_list.append(("elongation", "<=", self.info_elongation_max))
            domain_list.append(("elongation", ">=", self.info_elongation_min))

        if domain_list:
            production_lot_objs = self.env["stock.production.lot"]. \
                                search(domain_list)
            production_lot_objs_list = []
            context = dict(self._context)

            look_up_by_item = {}
            inventory_look_by_item_id = None
            for production_lot_obj in production_lot_objs:  
                production_lot_objs_list.append(production_lot_obj.id)
                if production_lot_obj.category_id:
                    look_up_by_item['info_category_id'] = production_lot_obj.category_id.id or production_lot_obj.category_id
                if production_lot_obj.sub_category_id:
                    look_up_by_item['info_sub_category_id'] = production_lot_obj.sub_category_id.id or production_lot_obj.sub_category_id
                if production_lot_obj.product_id:
                    look_up_by_item['info_sub_product_id'] = production_lot_obj.product_id.id or production_lot_obj.product_id
                if context.get('active_id'):
                    look_up_by_item['so_look_up_by_item_id'] = context.get('active_id')
                if production_lot_obj.stock_status:
                    look_up_by_item['info_stock_status'] = production_lot_obj.stock_status
                if production_lot_obj.thickness_mm:
                    look_up_by_item['info_thickness_min'] = production_lot_obj.thickness_mm
                if production_lot_obj.width_in:
                    look_up_by_item['info_width_min'] = production_lot_obj.width_in
                if production_lot_obj.length_mm:
                    look_up_by_item['info_length_min'] = production_lot_obj.length_mm
                if production_lot_obj.weight_lb:
                    look_up_by_item['info_weight_min'] = production_lot_obj.weight_lb
                if look_up_by_item and context.get('active_id'):
                    # print("if look_up_by_item and context.get('active_id'):===================")
                    inventory_look_by_item_id = self.env['inventory.look.up.by.item'].create(look_up_by_item)
                # return True
                # print("inventory_look_by_item_id=====================",inventory_look_by_item_id,self._context)
            # print("\n\n\nproduction_lot_objs_list================",production_lot_objs_list,self._context)
            #
            if production_lot_objs_list and not context.get('active_id') :
                return {
                    "type": "ir.actions.act_window",
                    "name": _("Lots/Serial Numbers"),
                    "res_model": "stock.production.lot",
                    "view_mode": "tree,form",
                    "domain":[("id","in",production_lot_objs_list)]
                   }

        return True

