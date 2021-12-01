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


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    # Header
    id_lot_stock = fields.Float(string="StockID")
    lot_od = fields.Float(string="OD")
    reserve_customer_id = fields.Many2one('res.partner',string="Reserve Customer")
    customer_po =fields.Char(string="Customer PO")
    release_no =fields.Char(string="Release No.")
    mill_tag_number=fields.Char(string="Mill Tag Number")
    res_guage_type = fields.Many2one('res.gauge.type',string="Gauge Type")
    res_grade = fields.Many2one('res.grade',string="Grade(M2O)")
    # Surface Finish
    res_nct_ct_id = fields.Many2one('res.nct.ct',string="NCT/CT")
    res_oil_dry_id= fields.Many2one('res.oil.dry',string="Oil/Dry")
    coating_weight = fields.Float('Coating Weight')
    spangle = fields.Float('Spangle')
    surface = fields.Float('Surface')
    res_edge_id = fields.Many2one('res.edge',string="Edge")
    process_undergone_ids = fields.Many2many('process.undergone',string="Process Undergone(M2M)")
    # Chemical Properties
    comp_fe = fields.Float(string="FE", digits=[4, 3])
    comp_mg = fields.Float(string="MG", digits=[4, 3])
    comp_co = fields.Float(string="Co", digits=[4, 3])
    comp_zn = fields.Float(string="Zn", digits=[4, 3])
    comp_cd = fields.Float(string="Cd", digits=[4, 3])
    comp_w = fields.Float(string="W", digits=[4, 3])
    comp_pb = fields.Float(string="Pb", digits=[4, 3])
    comp_bi = fields.Float(string="Bi", digits=[4, 3])
    comp_be = fields.Float(string="Be", digits=[4, 3])
    comp_as = fields.Float(string="As", digits=[4, 3])
    comp_se = fields.Float(string="Se", digits=[4, 3])
    comp_zr = fields.Float(string="Zr", digits=[4, 3])
    comp_ag = fields.Float(string="Ag", digits=[4, 3])
    comp_sb = fields.Float(string="Sb", digits=[4, 3])
    comp_au = fields.Float(string="Au", digits=[4, 3])
    comp_o = fields.Float(string="O", digits=[4, 3])
    comp_y = fields.Float(string="Y", digits=[4, 3])
    comp_h = fields.Float(string="H", digits=[4, 3])
    comp_nb_cb = fields.Float(string="Nc/CB", digits=[4, 3])
    soluble_aluminium = fields.Float(string="Soluble Aluminium(SA)", digits=[4, 3])
    carbon_equivalent = fields.Float(string="Carbon Equivalent(CZ)", digits=[4, 3])
    residual_hydrogen = fields.Float(string="Residual Hydrogen(RH)", digits=[4, 3])
    total_residual = fields.Float(string="Total Residual(TR)", digits=[4, 3])
    # Physical Properties
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
    # Purchase Details
    unit_cost = fields.Float("Unit Cost")
    purchase_cose_untexed = fields.Float("Total Purchase Cost(Untaxed)")
    purchase_cose_texed = fields.Float("Total Purchase Cost(Taxed)")
    certs = fields.Selection([('yes', 'Yes'),('no', 'No')], string='Certs')
    # Shipping Details
    ship_from_id = fields.Many2one('frm.location',string="Ship From")
    ship_to_id = fields.Many2one('frm.location',string="Ship To")
    ship_via_id = fields.Many2one('frm.mode.operation',string="Ship Via")
    purchase_incoterm_id = fields.Many2one('account.incoterms',string="Incoterm")
    fob = fields.Char(string="FOB")
    date_time_recevied = fields.Datetime(string="Date Received(Shipping Details)")
    # Quality Remarks
    visual_inspection_px = fields.Text(string="Visual Inspection")
