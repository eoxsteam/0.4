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

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    mill_tag_number = fields.Char(string="Mill Tag Number")
    vendor_tag_number = fields.Char(string="Vendor Tag No.")
    inventory_grade = fields.Char(string="Inventory Grade")
    finish=fields.Char(string="Finish")
    coating=fields.Char(string="Coating")
    rb_min=fields.Float(string="RB(min)")
    rb_max=fields.Float(string="RB(max)")
    olsen_min= fields.Float(string="Olsen(min)")
    olsen_max= fields.Float(string="Olsen(max)")
    gauge_min= fields.Float(string="Gauge(min)")
    gauge_max= fields.Float(string="Gauge(max)")
    width_min = fields.Float(string="Width(min)")
    width_max = fields.Float(string="Width(max)")
    length_min = fields.Float(string="Length(min)")
    length_max = fields.Float(string="Length(max)")
    length_tolerance_min = fields.Float(string="Length Tolerance(min)")
    length_tolerance_max = fields.Float(string="Length Tolerance(max)")
    sq_tolerance_min = fields.Float(string="Sq Tolerance High(min)")
    sq_tolerance_max = fields.Float(string="Sq Tolerance High(max)")
    id_min= fields.Float(string="ID(min)")
    id_max= fields.Float(string="ID(max)")
    od_min= fields.Float(string="OD(min)")
    od_max= fields.Float(string="OD(max)")
    coil_min= fields.Float(string="Coil(min)")
    coil_max= fields.Float(string="Coil(max)")
    max_lift = fields.Char(string="Max Lift")
    surface =fields.Char(string="Surface")
    mill_stencil=fields.Char(string="Mill Stencil")
    ductility=fields.Float(string="Ductility")
    part_category=fields.Char(string="Part Category")
    spangle=fields.Char(string="Spangle")
    coating_weight=fields.Float(string="Coating Weight")
    release_no=fields.Char(string="Release No.")
    reserve_customer_id=fields.Many2one("res.partner",string="Reserve Customer")
    condition=fields.Char(string="Condition")
    projection_number=fields.Char(string="Projection Number")
    res_nct_ct_id = fields.Many2one('res.nct.ct',string="NCT/CT")
    res_gauge_id = fields.Many2one('steel.gauge',string="Gauge")
    res_edge_id = fields.Many2one('res.edge',string="Edge")
    res_oil_dry_id= fields.Many2one('res.oil.dry',string="Oil/Dry")
    res_gauge_type_id= fields.Many2one('res.gauge.type',string="Gauge Type")
    res_receive_tag_id= fields.Many2one('res.receive.tag',string="Receive Tag As")
    res_yte_id= fields.Many2one('res.yte',string="YTE")
    res_dfars_domestic_id= fields.Many2one('res.dfars.domestic',string="DFARS or Domestic")
    # Chemical Properties
    chem_al = fields.Float(string="Al")
    chem_cu = fields.Float(string="Cu")
    chem_cr = fields.Float(string="Cr")
    chem_fe = fields.Float(string="Fe")
    chem_mg = fields.Float(string="Mg")
    chem_b = fields.Float(string="B")
    chem_c = fields.Float(string="C")
    chem_n = fields.Float(string="N")
    chem_si = fields.Float(string="Si")
    chem_p = fields.Float(string="P")
    chem_s = fields.Float(string="S")
    chem_ca = fields.Float(string="Ca")
    chem_ti = fields.Float(string="Ti")
    chem_mn = fields.Float(string="Mn")
    chem_co = fields.Float(string="Co")
    chem_ni = fields.Float(string="Ni")
    chem_zn = fields.Float(string="Zn")
    chem_nb_cb = fields.Float(string="Nb/Cb")
    chem_mo = fields.Float(string="Mo")
    chem_cd = fields.Float(string="Cd")
    chem_sn = fields.Float(string="Sn")
    chem_w = fields.Float(string="W")
    chem_pb = fields.Float(string="Pb")
    chem_bi = fields.Float(string="Bi")
    chem_be = fields.Float(string="Be")
    chem_as = fields.Float(string="As")
    chem_se = fields.Float(string="Se")
    chem_zr = fields.Float(string="Zr")
    chem_ag = fields.Float(string="Ag")
    chem_sb = fields.Float(string="Sb")
    chem_au = fields.Float(string="Au")
    chem_o = fields.Float(string="O")
    chem_v = fields.Float(string="V")
    chem_y = fields.Float(string="Y")
    chem_h = fields.Float(string="H")
    chem_soluble_aluminium = fields.Float(string="Soluble Aluminium(SA)")
    chem_carbon_equivalent = fields.Float(string="Carbon Equivalent(CZ))")
    chem_residual_hydrogen = fields.Float(string="Residual Hydrogen(RH)")
    chem_total_residual = fields.Float(string="Total Residual(TR)")
    # Physical Properties
    physical_yield = fields.Float(string="Yield")
    tensile = fields.Float(string="Tensile")
    elongation = fields.Float(string="Elongation")
    r_value = fields.Float(string="r value")
    n_value = fields.Float(string="n value")
    olsen_id = fields.Float(string="Olsen ID")
    olsen_od = fields.Float(string="Olsen OD")
    rb_id = fields.Float(string="RB ID")
    rb_od = fields.Float(string="RB OD")
    core_loss = fields.Float(string="Core Loss")
    permeability = fields.Float(string="Permeability")
    grain_size = fields.Float(string="Grain Size")
    r_o_a = fields.Float(string="R.O.A")
    hardenability = fields.Float(string="Hardenability")
    charpy = fields.Float(string="Charpy")
    olsen = fields.Float(string="Olsen")
    brinell = fields.Float(string="Brinell")
    ductility = fields.Float(string="Ductility")
    heat_no = fields.Float(string="Heat No.")
    #Packaging Instructions
    res_skid_cylinder_id=fields.Many2one('res.skid.cylinder',string="Skid/Cylinder")
    res_eye_pos =fields.Many2one('res.eye.pos',string="Eye Pos")
    res_crane =fields.Many2one('res.crane',string="Crane")
    wind=fields.Char(string="Wind")
    bands_id=fields.Float(string="Bands ID")
    bands_od=fields.Float(string="Bands OD")
    cores=fields.Float(string="Cores")
    interleave=fields.Char(string="Interleave")
    paper=fields.Char(string="Paper")
    vci_paper=fields.Char(string="VCI Paper")
    packaging_instructions=fields.Text(string="Packaging Instructions")
    edge_protection=fields.Char(string="Edge Protection") 
    package_type=fields.Char(string="Package Type")
    protect_id=fields.Float(string="Protect ID")
    protect_od=fields.Float(string="Protect OD")
    skids=fields.Float(string="Skids")
    skid_bands=fields.Float(string="Skid Bands")
    detailed_instructions=fields.Text(string="Detailed Instructions")
    thickness_min = fields.Float(string="Thickness Min")
    thickness_max = fields.Float(string="Thickness Max")
    po_weight = fields.Float(string='Weight')
    width_tolerance_min = fields.Float(string='Width Tolerance(min)', digits=[6, 4])
    width_tolerance_max = fields.Float(string='Width Tolerance(max)', digits=[6, 4])
    cwt_price = fields.Float(string='CWT Price', digits=[6, 2])


    @api.onchange('res_gauge_id')
    def _onchange_res_gauge_id(self):
        if self.res_gauge_id:
            self.thickness_in = self.res_gauge_id.gauge_inch
        else:
            self.thickness_in = 0.0     

    def _prepare_stock_moves(self, picking):
        res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
        res[0].update({'vendor_tag_number':self.vendor_tag_number,
                        'part_no':self.part_no,
                        'inventory_grade':self.inventory_grade,
                        'finish': self.finish,
                        'coating': self.coating,
                        'res_nct_ct_id': self.res_nct_ct_id and self.res_nct_ct_id.id or False,
                        'rb_min': self.rb_min,
                        'rb_max': self.rb_max,
                        'olsen_min': self.olsen_min,
                        'res_gauge_id': self.res_gauge_id and self.res_gauge_id.id or False,
                        'gauge_min': self.gauge_min,
                        'gauge_max': self.gauge_max,
                        'width_in': self.width_in,
                        'width_tolerance_min': self.width_tolerance_min,
                        'width_tolerance_max': self.width_tolerance_max,
                        'length_in': self.length_in,
                        'length_tolerance_max': self.length_tolerance_max,
                        'length_tolerance_min': self.length_tolerance_min,
                        'sq_tolerance_min': self.sq_tolerance_min,
                        'sq_tolerance_max': self.sq_tolerance_max,
                        'id_min': self.id_min,
                        'id_max': self.id_max,
                        'od_min': self.od_min,
                        'od_max': self.od_max,
                        'coil_max': self.coil_max,
                        'coil_min': self.coil_min,
                        'thickness_min': self.thickness_min,
                        'thickness_max': self.thickness_max,
                        'max_lift': self.max_lift,

                        'surface': self.surface,
                        'mill_stencil': self.mill_stencil,
                        'ductility': self.ductility,
                        'part_category': self.part_category,
                        'res_edge_id': self.res_edge_id and self.res_edge_id.id or False,
                        'spangle': self.spangle,
                        'coating_weight': self.coating_weight,
                        'res_oil_dry_id': self.res_oil_dry_id and self.res_oil_dry_id.id or False,
                        'res_gauge_type_id': self.res_gauge_type_id and self.res_gauge_type_id.id or False,
                        'res_receive_tag_id': self.res_receive_tag_id and self.res_receive_tag_id.id or False,
                        'certsreq': self.certsreq,
                        'res_yte_id': self.res_yte_id and self.res_yte_id.id or False,
                        'release_no': self.release_no,
                        'res_dfars_domestic_id': self.res_dfars_domestic_id and self.res_dfars_domestic_id.id or False,
                        'reserve_customer_id': self.reserve_customer_id and self.reserve_customer_id.id or False,
                        'condition': self.condition,
                        'projection_number': self.projection_number,
                        'chem_c': self.chem_c,
                        'chem_mn': self.chem_mn,
                        'chem_p': self.chem_p,
                        'chem_s': self.chem_s,
                        'chem_al': self.chem_al,
                        'chem_ti': self.chem_ti,
                        'chem_cu': self.chem_cu,
                        'chem_fe': self.chem_fe,
                        'chem_mg': self.chem_mg,
                        'chem_b': self.chem_b,
                        'chem_si': self.chem_si,
                        'chem_n': self.chem_n,
                        'chem_ca': self.chem_ca,
                        'chem_co': self.chem_co,
                        'chem_ni': self.chem_ni,
                        'chem_zn': self.chem_zn,
                        'chem_nb_cb': self.chem_nb_cb,
                        'chem_soluble_aluminium': self.chem_soluble_aluminium,
                        'chem_carbon_equivalent': self.chem_carbon_equivalent,
                        'chem_residual_hydrogen': self.chem_residual_hydrogen,

                        'chem_total_residual': self.chem_total_residual,
                        'physical_yield': self.physical_yield,
                        'tensile': self.tensile,
                        'elongation': self.elongation,
                        'r_value': self.r_value,
                        'n_value': self.n_value,
                        'olsen_id': self.olsen_id,
                        'olsen_od': self.olsen_od,
                        'rb_id': self.rb_id,
                        'rb_od': self.rb_od,
                        'core_loss': self.core_loss,
                        'permeability': self.permeability,
                        'grain_size': self.grain_size,
                        'r_o_a': self.r_o_a,
                        'hardenability': self.hardenability,
                        'charpy': self.charpy,
                        'olsen': self.olsen,
                        'brinell': self.brinell,
                        'ductility': self.ductility,
                        'heat_no': self.heat_no,
                        'res_skid_cylinder_id': self.res_skid_cylinder_id and self.res_skid_cylinder_id.id or False,
                        'res_eye_pos': self.res_eye_pos and self.res_eye_pos.id or False,
                        'wind': self.wind,
                        'spacers': self.spacers,
                        'bands_id': self.bands_id,
                        'bands_od': self.bands_od,
                        'cores': self.cores,
                        'interleave': self.interleave,
                        'paper': self.paper,
                        'vci_paper': self.vci_paper,
                        'packaging_instructions': self.packaging_instructions,
                        'edge_protection': self.edge_protection,
                        'package_type': self.package_type,
                        'protect_id': self.protect_id,
                        'protect_od': self.protect_od,
                        'skids': self.skids,
                        'skid_bands': self.skid_bands,
                        'res_crane': self.res_crane and self.res_crane.id or False,
                        'fork_lift': self.fork_lift,
                        'detailed_instructions': self.detailed_instructions,
                        'cwt_price':self.cwt_price,
                        

                    })
        return res

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_ids = fields.Many2many('sale.order', string='Sale Order Reference')
