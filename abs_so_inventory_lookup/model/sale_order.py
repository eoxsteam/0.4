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

from odoo import api, models, fields, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    client_order_ref = fields.Char(string='Customer ID', copy=False)

    inventory_look_up_by_item_ids = fields.One2many('inventory.look.up.by.item', 'so_look_up_by_item_id',
                                                    'By Item', ondelete='set null')
    inventory_look_up_by_chemistries_ids = fields.One2many('inventory.look.up.by.chemistries', 'so_look_up_by_chemistries_id',
                                                           'By Chemistries', ondelete='set null')


    def button_inventory_lookup_by_item(self):
        return {
            "name": _("By Item Info"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "by.item.info.wizard",
            "views": [(False, "form")],
            "view_id": self.env.ref("abs_inventory_lookup.view_by_item_info_form",
                                    "False"),
            "target": "new",
            "binding_view_types": "form"
        }

    def button_inventory_lookup_by_chemistries(self):
        return {
            "name": _("By Chemistries"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "by.chemistries.wizard",
            "views": [(False, "form")],
            "view_id": self.env.ref("abs_inventory_lookup.view_by_chemistries_form",
                                    "False"),
            "target": "new",
            "binding_view_types": "form"
        }






class InventoryLookUPByTtem(models.Model):
    _name = "inventory.look.up.by.item"
    _description = "Inventory Look UP By Ttem"

    so_look_up_by_item_id = fields.Many2one("sale.order",
                                            string="SO Master")
    info_category_id = fields.Many2one("product.category",
                                       string="Master")
    info_sub_category_id = fields.Many2one("product.category",
                                           string="Sub Category")
    info_sub_product_id = fields.Many2one("product.product",
                                          string="Sub Product")
    info_partner_id = fields.Many2one("res.partner",
                                      string="Vendor")
    info_partner_no_id = fields.Char(string="Vendor No",
                                     related="info_partner_id.vendor_serial_number")
    info_partner_reserver_id = fields.Many2one("res.partner",
                                               string="Reserve Customer")
    info_gauge_min = fields.Integer(string="Gauge(Min-Max)")
    info_gauge_max = fields.Integer(string="Gauge-Max")
    info_thickness_min = fields.Float(string="Thickness(Min-Max)")
    info_thickness_max = fields.Float(string="Thickness-Max")
    info_width_min = fields.Float(string="Width(Min-Max)")
    info_width_max = fields.Float(string="Width-Max")
    info_width_selection = fields.Selection([("mm", "MM"),
                                             ("in", "IN")],
                                            string="MM/IN",
                                            default="mm")
    info_length_min = fields.Float(string="Length(Min-Max)")
    info_length_max = fields.Float(string="Length-Max")
    info_len_selection = fields.Selection([("mm", "MM"),
                                           ("in", "IN")],
                                          string="Len MM/IN",
                                          default="mm")
    info_weight_min = fields.Integer(string="Weight(Min-Max)")
    info_weight_max = fields.Integer(string="Weight-Max")
    info_weight_selection = fields.Selection([("lbs", "Lbs"),
                                              ("kg", "KG")],
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
    info_yield_selection = fields.Selection([("mpa", "MPA"),
                                             ("psi", "PSI"),
                                             ("ksi", "KSI")],
                                            string="MPS/PSI/KSI",
                                            default="mpa")
    info_tensile_min = fields.Float(string="Tensile(Min-Max)")
    info_tensile_max = fields.Float(string="Tensile-Max")
    info_tensile_selection = fields.Selection([("mpa", "MPA"),
                                               ("psi", "PSI"),
                                               ("ksi", "KSI")],
                                              string="Tensile MPS/PSI/KSI",
                                              default="mpa")
    info_elongation_min = fields.Float(string="Elongation(Min-Max)")
    info_elongation_max = fields.Float(string="Elongation-Max")
    info_received = fields.Selection([("received", "Received"),
                                      ("sold", "Sold")],
                                     string="Received", ondelete='set null')
    info_start_date = fields.Date(string="Received Date")
    info_end_date = fields.Date(string="Sold Date")
    info_stock_status = fields.Selection([("transit", "In Transit"),
                                          ("available", "Available"),
                                          ("reserved", "Reserved"),
                                          ("in_production", "In production"),
                                          ("not_available", "Not available")],
                                         string="Stock Status", ondelete='set null')


class IventoryLookUpByChemistries(models.Model):
    _name = "inventory.look.up.by.chemistries"
    _description = "Iventory Look Up By Chemistries"

    so_look_up_by_chemistries_id = fields.Many2one("sale.order",
                                                   string="SO Master")
    chem_category_id = fields.Many2one("product.category",
                                       string="Chem Master")
    chem_sub_category_id = fields.Many2one("product.category",
                                           string="Chem Sub Category")
    chem_sub_product_id = fields.Many2one("product.product",
                                          string="Chem Sub Product")
    chem_partner_id = fields.Many2one("res.partner",
                                      string="Chem Vendor")
    chem_partner_no_id = fields.Char(string="Chem Vendor No",
                                     related="chem_partner_id.name")
    chem_partner_reserver_id = fields.Many2one("res.partner",
                                               string="Chem Reserve Customer")
    chem_gauge_min = fields.Integer(string="Chem Gauge(Min-Max)")
    chem_gauge_max = fields.Integer(string="Chem Gauge-Max")
    chem_thickness_min = fields.Float(string="Chem Thickness(Min-Max)")
    chem_thickness_max = fields.Float(string="Chem Thickness-Max")
    chem_width_min = fields.Float(string="Chem Width(Min-Max)")
    chem_width_max = fields.Float(string="Chem Width-Max")
    chem_width_selection = fields.Selection([("mm", "MM"),
                                             ("in", "IN")],
                                            string="Chem MM/IN",
                                            default="mm")
    chem_length_min = fields.Float(string="Chem Length(Min-Max)")
    chem_length_max = fields.Float(string="Chem Length-Max")
    chem_len_selection = fields.Selection([("mm", "MM"),
                                           ("in", "IN")],
                                          string="Chem Len MM/IN",
                                          default="mm")
    chem_weight_min = fields.Integer(string="Chem Weight(Min-Max)")
    chem_weight_max = fields.Integer(string="Chem Weight-Max")
    chem_weight_selection = fields.Selection([("lbs", "Lbs"),
                                              ("kg", "KG")],
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
    chem_yield_selection = fields.Selection([("mpa", "MPA"),
                                             ("psi", "PSI"),
                                             ("ksi", "KSI")],
                                            string="Chem MPS/PSI/KSI",
                                            default="mpa")
    chem_tensile_min = fields.Float(string="Chem Tensile(Min-Max)")
    chem_tensile_max = fields.Float(string="Chem Tensile-Max")
    chem_tensile_selection = fields.Selection([("mpa", "MPA"),
                                               ("psi", "PSI"),
                                               ("ksi", "KSI")],
                                              string="Chem Ten MPS/PSI/KSI",
                                              default="mpa")
    chem_elongation_min = fields.Float(string="Chem Elongation(Min-Max)")
    chem_elongation_max = fields.Float(string="Chem Elongation-Max")
    chem_received = fields.Selection([("received", "Received"),
                                      ("sold", "Sold")],
                                     string="Chem Received", ondelete='set null')
    chem_start_date = fields.Date(string="Chem Received Date")
    chem_end_date = fields.Date(string="Chem Sold Date")
    chem_stock_status = fields.Selection([("transit", "In Transit"),
                                          ("available", "Available"),
                                          ("reserved", "Reserved"),
                                          ("in_production", "In production"),
                                          ("not_available", "Not available")],
                                         string="Chem Stock Status",ondelete='set null')
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
