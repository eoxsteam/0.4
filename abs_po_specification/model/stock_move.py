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

class StockMove(models.Model):
    _inherit = "stock.move"

    res_gauge_id = fields.Many2one('steel.gauge',string="Gauge")
    width_in = fields.Float(string='Width(in)', digits=[6, 4])
    thickness_in = fields.Float(string='Thickness(in)', digits=[6, 4])
    length_in = fields.Float(string='Length(in)', digits=[6, 4])
    cwt_price = fields.Float(string='CWT Price', digits=[6, 2])
    thickness_min = fields.Float(string="Thickness Min")
    thickness_max = fields.Float(string="Thickness Max")
    product_category_id = fields.Many2one('product.category', 'Category', domain="[('parent_id', '=', False)]")
    

# class StockPicking(models.Model):
#     _inherit = "stock.picking"

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
    # res_gauge_id = fields.Many2one('steel.gauge',string="Gauge")
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

    width_tolerance_min = fields.Float(string='Width Tolerance(min)', digits=[6, 4])
    width_tolerance_max = fields.Float(string='Width Tolerance(max)', digits=[6, 4])
    gauge_tolerance_min = fields.Float(string='Gauge Tolerance(min)')
    gauge_tolerance_max = fields.Float(string='Gauge Tolerance(max)')
    dia_id = fields.Float(string='ID')
    dia_od_min = fields.Float(string='OD(min)')
    dia_od_max = fields.Float(string='OD(min)')
    rockwell_min = fields.Float(string='Rockwell(min)', digits=[6, 1])
    rockwell_max = fields.Float(string='Rockwell(max)', digits=[6, 1])
    part_no = fields.Text(string='Part Number')
    fork_lift = fields.Text(string='Forklift')
    certsreq = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='CertsReq ', default='yes')
    spacers = fields.Integer(string='Spacers ')
    mx_skid_wt = fields.Char(string='Max Skid Wt.')
    over_head_crar = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Over Head Crar', default='yes')
    width_in = fields.Float(string='Width(in)', digits=[6, 4])
    length_in = fields.Float(string='Length(in)', digits=[6, 4])

    def action_view_move(self):
        action = {
            'type': 'ir.actions.act_window',
            'views': [(self.env.ref('abs_po_specification.button_stock_move_form').id, 'form')],
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'name': _('Stock Moves'),
            'res_model': 'stock.move', }
        return action