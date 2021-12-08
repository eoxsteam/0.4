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

class ByChemistriesWizard(models.TransientModel):
    _name = "by.chemistries.wizard"
    _description = "By Chemistries Wizard"

    chem_category_id = fields.Many2one("product.category",
                                       string="Chem Master",domain="[('parent_id', '=', False)]")
    chem_sub_category_id = fields.Many2one("product.category",
                                           string="Chem Sub Category", domain="[('parent_id', '!=', False)]")
    chem_sub_product_id = fields.Many2one("product.product",
                                          string="Chem Sub Product")
    chem_partner_id = fields.Many2one("res.partner",
                                      string="Chem Vendor")
    chem_partner_no_id = fields.Char(string="Chem Vendor No",
                                     related="chem_partner_id.name")
    chem_partner_reserver_id = fields.Many2one("res.partner",
                                               string="Chem Reserve Customer")
    # chem_gauge_min = fields.Integer(string="Chem Gauge(Min-Max)")
    # chem_gauge_max = fields.Integer(string="Chem Gauge-Max")
    chem_gauge_min = fields.Many2many('steel.gauge', string="Thickness(Min-Max)")
    chem_thickness_min = fields.Float(string="Chem Thickness(Min-Max)")
    chem_thickness_max = fields.Float(string="Chem Thickness-Max")
    chem_width_min = fields.Float(string="Chem Width(Min-Max)")     
    chem_width_max = fields.Float(string="Chem Width-Max")
    chem_width_selection = fields.Selection([("mm","MM"),
                                            ("in","IN")],
                                            string="Chem MM/IN",
                                             default="mm") 
    chem_length_min = fields.Float(string="Chem Length(Min-Max)")     
    chem_length_max = fields.Float(string="Chem Length-Max")
    chem_len_selection = fields.Selection([("mm","MM"),
                                          ("in","IN")],
                                          string="Chem Len MM/IN",
                                          default="mm") 
    chem_weight_min = fields.Integer(string="Chem Weight(Min-Max)")
    chem_weight_max = fields.Integer(string="Chem Weight-Max")
    chem_weight_selection = fields.Selection([("lbs","Lbs"),
                                             ("kg","KG")],
                                             string="Chem LBS/KG",
                                             default="lbs") 
    chem_nct_id = fields.Many2one("res.nct.ct",
                                  string="Chem NCT/CT")
    chem_oil_id = fields.Many2one("res.oil.dry",
                                 string="Chem Dry/Oil")
    chem_id_gauge_min = fields.Integer(string="Chem ID Gauge(Min-Max)")
    chem_id_gauge_max = fields.Integer(string="Chem ID Gauge-Max")
    chem_od_gauge_min = fields.Integer(string="Chem OD Gauge(Min-Max)")
    chem_od_gauge_max = fields.Integer(string="Chem OD Gauge-Max")
    chem_piw_min = fields.Float(string="Chem PIW(Min-Max)")     
    chem_piw_max = fields.Float(string="Chem PIW-Max")
    chem_yield_min = fields.Float(string="Chem Yield(Min-Max)")     
    chem_yield_max = fields.Float(string="Chem Yield-Max")
    chem_yield_selection = fields.Selection([("mpa","MPA"),
                                            ("psi","PSI"),
                                            ("ksi","KSI")],
                                            string="Chem MPS/PSI/KSI",
                                            default="mpa") 
    chem_tensile_min = fields.Float(string="Chem Tensile(Min-Max)")     
    chem_tensile_max = fields.Float(string="Chem Tensile-Max")
    chem_tensile_selection = fields.Selection([("mpa","MPA"),
                                        ("psi","PSI"),
                                        ("ksi","KSI")],
                                        string="Chem Ten MPS/PSI/KSI",
                                        default="mpa")
    chem_elongation_min = fields.Float(string="Chem Elongation(Min-Max)")     
    chem_elongation_max = fields.Float(string="Chem Elongation-Max")
    chem_received = fields.Selection([("received","Received"),
                                     ("sold","Sold")],
                                     string="Chem Received")
    chem_start_date = fields.Date(string="Chem Received Date")
    chem_end_date = fields.Date(string="Chem Sold Date")
    chem_stock_status = fields.Selection([("transit","In Transit"),
                                         ("available","Available"),
                                         ("reserved","Reserved"),
                                         ("in_production","In production"),
                                         ("not_available","Not available")],
                                         string="Chem Stock Status")
    # Chemistries Property
    chem_al_min = fields.Float(string="Al(Min-Max)") 
    chem_al_max = fields.Float(string="Al-Max")
    chem_cu_min = fields.Float(string="Cu(Min-Max)") 
    chem_cu_max = fields.Float(string="Cu-Max")
    chem_cr_min = fields.Float(string="Cr(Min-Max)") 
    chem_cr_max = fields.Float(string="Cr-Max")
    chem_fe_min = fields.Float(string="Fe(Min-Max)") 
    chem_fe_max = fields.Float(string="Fe-Max")
    chem_mg_min = fields.Float(string="MG(Min-Max)") 
    chem_mg_max = fields.Float(string="MG-Max")
    chem_b_min = fields.Float(string="B(Min-Max)") 
    chem_b_max = fields.Float(string="B-Max")
    chem_c_min = fields.Float(string="C(Min-Max)") 
    chem_c_max = fields.Float(string="C-Max")
    chem_n_min = fields.Float(string="N(Min-Max)") 
    chem_n_max = fields.Float(string="N-Max")
    chem_si_min = fields.Float(string="Si(Min-Max)") 
    chem_si_max = fields.Float(string="si-Max")
    chem_p_min = fields.Float(string="P(Min-Max)") 
    chem_p_max = fields.Float(string="P-Max")
    chem_s_min = fields.Float(string="S(Min-Max)") 
    chem_s_max = fields.Float(string="s-Max")
    chem_ca_min = fields.Float(string="Ca(Min-Max)") 
    chem_ca_max = fields.Float(string="Ca-Max")
    chem_ti_min = fields.Float(string="Ti(Min-Max)") 
    chem_ti_max = fields.Float(string="Ti-Max")
    chem_mn_min = fields.Float(string="Mn(Min-Max)") 
    chem_mn_max = fields.Float(string="Mn-Max")
    chem_co_min = fields.Float(string="Co(Min-Max)") 
    chem_co_max = fields.Float(string="Co-Max")
    chem_ni_min = fields.Float(string="Ni(Min-Max)") 
    chem_ni_max = fields.Float(string="Ni-Max") 
    chem_mo_min = fields.Float(string="Mo(Min-Max)") 
    chem_mo_max = fields.Float(string="Mo-Max") 
    chem_cd_min = fields.Float(string="Cd(Min-Max)") 
    chem_cd_max = fields.Float(string="Cd-Max")
    chem_sn_min = fields.Float(string="Sn(Min-Max)") 
    chem_sn_max = fields.Float(string="Sn-Max")
    chem_w_min = fields.Float(string="W(Min-Max)") 
    chem_w_max = fields.Float(string="W-Max")  
    chem_pb_min = fields.Float(string="Pb(Min-Max)") 
    chem_pb_max = fields.Float(string="Pb-Max")
    chem_bi_min = fields.Float(string="Bi(Min-Max)") 
    chem_bi_max = fields.Float(string="Bi-Max")
    chem_be_min = fields.Float(string="Be(Min-Max)") 
    chem_be_max = fields.Float(string="Be-Max")
    chem_as_min = fields.Float(string="As(Min-Max)") 
    chem_as_max = fields.Float(string="As-Max")
    chem_se_min = fields.Float(string="Se(Min-Max)") 
    chem_se_max = fields.Float(string="Se-Max")
    chem_zr_min = fields.Float(string="Zr(Min-Max)") 
    chem_zr_max = fields.Float(string="Zr-Max")
    chem_ag_min = fields.Float(string="AG(Min-Max)") 
    chem_ag_max = fields.Float(string="Ag-Max")
    chem_sb_min = fields.Float(string="Sb(Min-Max)") 
    chem_sb_max = fields.Float(string="Sb-Max")
    chem_au_min = fields.Float(string="AU(Min-Max)") 
    chem_au_max = fields.Float(string="AU-Max")
    chem_zn_min = fields.Float(string="Zn(Min-Max)") 
    chem_zn_max = fields.Float(string="Zn-Max")
    chem_v_min = fields.Float(string="V(Min-Max)") 
    chem_v_max = fields.Float(string="V-Max")
    chem_nb_cb_min = fields.Float(string="Nb/Cb(Min-Max)") 
    chem_nb_cb_max = fields.Float(string="Nb/Cb-Max")

    @api.onchange('chem_sub_category_id')
    def onchange_chem_sub_category_id(self):
        for rec in self:
            return {'domain': {'chem_sub_product_id': [('categ_id', '=', rec.chem_sub_category_id.id)]}}

    def button_by_chemistries_search(self):
        domain_list = []
        if self.chem_al_min and self.chem_al_max:
            domain_list.append(("comp_al",">=",self.chem_al_min))
            domain_list.append(("comp_al","<=",self.chem_al_max))
        if self.chem_cu_min and self.chem_cu_max:
            domain_list.append(("comp_cu",">=",self.chem_cu_min))
            domain_list.append(("comp_cu","<=",self.chem_cu_max))
        if self.chem_cr_min and self.chem_cr_max:
            domain_list.append(("comp_cr",">=",self.chem_cr_min))
            domain_list.append(("comp_cr","<=",self.chem_cr_max))
        if self.chem_fe_min and self.chem_fe_max:
            domain_list.append(("comp_fe",">=",self.chem_fe_min))
            domain_list.append(("comp_fe","<=",self.chem_fe_max))
        if self.chem_mg_min and self.chem_mg_max:
            domain_list.append(("comp_mg",">=",self.chem_mg_min))
            domain_list.append(("comp_mg","<=",self.chem_mg_max))
        if self.chem_b_min and self.chem_b_max:
            domain_list.append(("comp_b",">=",self.chem_b_min))
            domain_list.append(("comp_b","<=",self.chem_b_max))
        if self.chem_c_min and self.chem_c_max:
            domain_list.append(("comp_c",">=",self.chem_c_min))
            domain_list.append(("comp_c","<=",self.chem_c_max))
        if self.chem_n_min and self.chem_n_max:
            domain_list.append(("comp_n",">=",self.chem_n_min))
            domain_list.append(("comp_n","<=",self.chem_n_max))
        if self.chem_si_min and self.chem_si_max:
            domain_list.append(("comp_si",">=",self.chem_si_min))
            domain_list.append(("comp_si","<=",self.chem_si_max))
        if self.chem_p_min and self.chem_p_max:
            domain_list.append(("comp_p",">=",self.chem_p_min))
            domain_list.append(("comp_p","<=",self.chem_p_max))
        if self.chem_s_min and self.chem_s_max:
            domain_list.append(("comp_s",">=",self.chem_s_min))
            domain_list.append(("comp_s","<=",self.chem_s_max))
        if self.chem_ca_min and self.chem_ca_max:
            domain_list.append(("comp_ca",">=",self.chem_ca_min))
            domain_list.append(("comp_ca","<=",self.chem_ca_max))
        if self.chem_ti_min and self.chem_ti_max:
            domain_list.append(("comp_ti",">=",self.chem_ti_min))
            domain_list.append(("comp_ti","<=",self.chem_ti_max))
        if self.chem_mn_min and self.chem_mn_max:
            domain_list.append(("comp_mn",">=",self.chem_mn_min))
            domain_list.append(("comp_mn","<=",self.chem_mn_max))
        if self.chem_co_min and self.chem_co_max:
            domain_list.append(("comp_co",">=",self.chem_co_min))
            domain_list.append(("comp_co","<=",self.chem_co_max))
        if self.chem_ni_min and self.chem_ni_max:
            domain_list.append(("comp_ni",">=",self.chem_ni_min))
            domain_list.append(("comp_ni","<=",self.chem_ni_max))
        if self.chem_mo_min and self.chem_mo_max:
            domain_list.append(("comp_mo",">=",self.chem_mo_min))
            domain_list.append(("comp_mo","<=",self.chem_mo_max))
        if self.chem_cd_min and self.chem_cd_max:
            domain_list.append(("comp_cd",">=",self.chem_cd_min))
            domain_list.append(("comp_cd","<=",self.chem_cd_max))
        if self.chem_sn_min and self.chem_sn_max:
            domain_list.append(("comp_sn",">=",self.chem_sn_min))
            domain_list.append(("comp_sn","<=",self.chem_sn_max))
        if self.chem_w_min and self.chem_w_max:
            domain_list.append(("comp_w",">=",self.chem_w_min))
            domain_list.append(("comp_w","<=",self.chem_w_max))
        if self.chem_pb_min and self.chem_pb_max:
            domain_list.append(("comp_pb",">=",self.chem_pb_min))
            domain_list.append(("comp_pb","<=",self.chem_pb_max))
        if self.chem_bi_min and self.chem_bi_max:
            domain_list.append(("comp_bi",">=",self.chem_bi_min))
            domain_list.append(("comp_bi","<=",self.chem_bi_max))
        if self.chem_be_min and self.chem_be_max:
            domain_list.append(("comp_be",">=",self.chem_be_min))
            domain_list.append(("comp_be","<=",self.chem_be_max))
        if self.chem_as_min and self.chem_as_max:
            domain_list.append(("comp_as",">=",self.chem_as_min))
            domain_list.append(("comp_as","<=",self.chem_as_max))
        if self.chem_se_min and self.chem_se_max:
            domain_list.append(("comp_se",">=",self.chem_se_min))
            domain_list.append(("comp_se","<=",self.chem_se_max))
        if self.chem_zr_min and self.chem_zr_max:
            domain_list.append(("comp_zr",">=",self.chem_zr_min))
            domain_list.append(("comp_zr","<=",self.chem_zr_max))
        if self.chem_ag_min and self.chem_ag_max:
            domain_list.append(("comp_ag",">=",self.chem_ag_min))
            domain_list.append(("comp_ag","<=",self.chem_ag_max))
        if self.chem_sb_min and self.chem_sb_max:
            domain_list.append(("comp_sb",">=",self.chem_sb_min))
            domain_list.append(("comp_sb","<=",self.chem_sb_max))
        if self.chem_au_min and self.chem_au_max:
            domain_list.append(("comp_au",">=",self.chem_au_min))
            domain_list.append(("comp_au","<=",self.chem_au_max))
        if self.chem_zn_min and self.chem_zn_max:
            domain_list.append(("comp_zn",">=",self.chem_zn_min))
            domain_list.append(("comp_zn","<=",self.chem_zn_max))
        if self.chem_v_min and self.chem_v_max:
            domain_list.append(("comp_v",">=",self.chem_v_min))
            domain_list.append(("comp_v","<=",self.chem_v_max))
        if self.chem_nb_cb_min and self.chem_nb_cb_max:
            domain_list.append(("comp_nb_cb",">=",self.chem_nb_cb_min))
            domain_list.append(("comp_nb_cb","<=",self.chem_nb_cb_max))
        
        if self.chem_category_id:
            domain_list.append(("category_id.id",
                                "=",
                                self.chem_category_id.id))
        if self.chem_sub_category_id:
            domain_list.append(("sub_category_id.id",
                                "=",
                                self.chem_sub_category_id.id))
        if self.chem_sub_product_id:
            domain_list.append(("product_id.id",
                                "=",
                                self.chem_sub_product_id.id))
        if self.chem_partner_reserver_id:
            domain_list.append(("reserve_customer_id.id",
                                "=",
                                self.chem_partner_reserver_id.id))
        if self.chem_partner_id:
            domain_list.append(("vendor_id.id",
                                "=",
                                self.chem_partner_id.id))
        if self.chem_nct_id:
            domain_list.append(("res_nct_ct_id.id",
                                "=",
                                self.chem_nct_id.id))
        if self.chem_oil_id:
            domain_list.append(("res_oil_dry_id.id",
                                "=",
                                self.chem_oil_id.id))
        if self.chem_stock_status:
            domain_list.append(("stock_status",
                                "=",
                                self.chem_stock_status))

        if self.chem_thickness_min and self.chem_thickness_max:
            domain_list.append(("thickness_mm", ">=", self.chem_thickness_min))
            domain_list.append(("thickness_mm", "<=", self.chem_thickness_max))
        
        if self.chem_width_min and self.chem_width_max:
            if self.chem_width_selection == "mm":
                domain_list.append(("width_mm", ">=", self.chem_width_min))
                domain_list.append(("width_mm", "<=", self.chem_width_max))
            else:
                domain_list.append(("width_in", ">=", self.chem_width_min))
                domain_list.append(("width_in", "<=", self.chem_width_max))

        if self.chem_length_min and self.chem_length_max:
            if self.chem_len_selection == "mm":
                domain_list.append(("length_mm", ">=", self.chem_length_min))
                domain_list.append(("length_mm", "<=", self.chem_length_max))
            else:
                domain_list.append(("length_in", ">=", self.chem_length_min))
                domain_list.append(("length_in", "<=", self.chem_length_max))
      
        if self.chem_weight_min and self.chem_weight_max:
            if self.chem_weight_selection == "lbs":
                domain_list.append(("weight_lb", ">=", self.chem_weight_min))
                domain_list.append(("weight_lb", "<=", self.chem_weight_max))
            else:
                # 1kg = 2.20462262185 lbs
                min_lbs = self.chem_weight_min * 2.20462262185  
                max_lbs = self.chem_weight_max * 2.20462262185
                domain_list.append(("weight_lb", ">=", min_lbs))
                domain_list.append(("weight_lb", "<=", max_lbs))
 
        """if self.chem_piw_min and self.chem_piw_max:
            domain_list.append(("piw", ">=", self.chem_piw_min))
            domain_list.append(("piw", "<=", self.chem_piw_max))"""

        if self.chem_id_gauge_min and self.chem_id_gauge_max:
            domain_list.append(("id_lot_stock", ">=", self.chem_id_gauge_min))
            domain_list.append(("id_lot_stock", "<=", self.chem_id_gauge_max))

        if self.chem_od_gauge_min and self.chem_od_gauge_max:
            domain_list.append(("lot_od", ">=", self.chem_od_gauge_min))
            domain_list.append(("lot_od", "<=", self.chem_od_gauge_max))

        if self.chem_yield_min and self.chem_yield_max:
            if self.chem_yield_selection == "mpa":
                domain_list.append(("yield_mpa", ">=", self.chem_yield_min))
                domain_list.append(("yield_mpa", "<=", self.chem_yield_max))
            elif self.chem_yield_selection == "psi":
                domain_list.append(("yield_psi", ">=", self.chem_yield_min))
                domain_list.append(("yield_psi", "<=", self.chem_yield_max))
            elif self.chem_yield_selection == "ksi":
                domain_list.append(("yield_ksi", ">=", self.chem_yield_min))
                domain_list.append(("yield_ksi", "<=", self.chem_yield_max))

        if self.chem_tensile_min and self.chem_tensile_max:
            if self.chem_tensile_selection == "mpa":
                domain_list.append(("tensile_mpa", ">=", self.chem_tensile_min))
                domain_list.append(("tensile_mpa", "<=", self.chem_tensile_max))
            elif self.chem_tensile_selection == "psi":
                domain_list.append(("tensile_psi", ">=", self.chem_tensile_min))
                domain_list.append(("tensile_psi", "<=", self.chem_tensile_max))
            elif self.chem_tensile_selection == "ksi":
                domain_list.append(("tensile_ksi", ">=", self.chem_tensile_min))
                domain_list.append(("tensile_ksi", "<=", self.chem_tensile_max))
         
        if self.chem_elongation_min and self.chem_elongation_max:
            domain_list.append(("elongation", ">=", self.chem_elongation_min))
            domain_list.append(("elongation", "<=", self.chem_elongation_max))

        if domain_list:
            production_lot_objs = self.env["stock.production.lot"].\
                                  search(domain_list)
            production_lot_obj_lst=[]
            look_up_by_chemistries = {}
            inventory_look_by_chemistries_id = None
            context = dict(self._context)
            for production_lot_obj in production_lot_objs:
                if production_lot_obj.category_id:
                    look_up_by_chemistries['chem_category_id'] = production_lot_obj.category_id.id or production_lot_obj.category_id
                if production_lot_obj.sub_category_id:
                    look_up_by_chemistries['chem_sub_category_id'] = production_lot_obj.sub_category_id.id or production_lot_obj.sub_category_id
                if production_lot_obj.product_id:
                    look_up_by_chemistries['chem_sub_product_id'] = production_lot_obj.product_id.id or production_lot_obj.product_id
                if context.get('active_id'):
                    look_up_by_chemistries['so_look_up_by_chemistries_id'] = context.get('active_id')
                if production_lot_obj.stock_status:
                    look_up_by_chemistries['chem_stock_status'] = production_lot_obj.stock_status
                if production_lot_obj.thickness_mm:
                    look_up_by_chemistries['chem_thickness_min'] = production_lot_obj.thickness_mm
                if production_lot_obj.width_in:
                    look_up_by_chemistries['chem_width_min'] = production_lot_obj.width_in
                if production_lot_obj.length_mm:
                    look_up_by_chemistries['chem_length_min'] = production_lot_obj.length_mm
                if production_lot_obj.weight_lb:
                    look_up_by_chemistries['chem_weight_min'] = production_lot_obj.weight_lb
                if look_up_by_chemistries and context.get('active_id'):
                    inventory_look_by_chemistries_id = self.env['inventory.look.up.by.chemistries'].create(look_up_by_chemistries)
                    # print("inventory_look_by_item_id=====================",inventory_look_by_chemistries_id,self._context)
                    production_lot_obj_lst.append(production_lot_obj.id)

            if production_lot_obj_lst and not context.get('active_id'):
                return {
                        "name": _("Lots/Serial Numbers"),
                        "type": "ir.actions.act_window",
                        "view_mode": "tree,form",
                        "res_model": "stock.production.lot",
                        "domain":[("id","in",production_lot_obj_lst)]
                       }

        return True
