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

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    res_receiving_hours_id = fields.Many2one("res.receiving.hours.time.range",
                                             string="Receiving Hours")
    res_receiving_day_id = fields.Many2one("res.receiving.week.day.range",
                                           string="Day Range")
    max_bundle_weight = fields.Float(string="Max. Bundle Weight")
    crane_id = fields.Many2one("res.crane",
                               string="Crane"
                               )
    forklift = fields.Char(string="Forklift")
    release_no = fields.Char(string="Release No")
    ship_to = fields.Char(string="Ship To")
    receiving_hours = fields.Char(string="Receiving Hours")
    receiving_time = fields.Char(string="Receiving Time")
    receiving_day = fields.Char(string="Receiving Day")

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        if self.partner_id \
           and self.partner_id.res_receiving_hours_id \
           and self.partner_id.res_receiving_day_id:
            self.res_receiving_hours_id = self.partner_id.res_receiving_hours_id
            self.res_receiving_day_id = self.partner_id.res_receiving_day_id
        else:
            self.res_receiving_hours_id = False
            self.res_receiving_day_id = False          

    	
