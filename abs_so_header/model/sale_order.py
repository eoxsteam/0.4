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

    credit_limit=fields.Float(string="Credit Approved")
    order_type = fields.Selection([("mat","MAT"),("prc","PRC")],
                                    string="Order Type")
    customer_po_number = fields.Char(string="Customer PO Number")
    order_due_date = fields.Date(string="Order Due Date")
    hot = fields.Boolean(string="Hot")
    res_receiving_hours_id = fields.Many2one("res.receiving.hours.time.range",
                                             string="Receiving Hours")
    res_receiving_day_id = fields.Many2one("res.receiving.week.day.range",
                                           string="Day Range")

    @api.onchange('partner_id')
    def onchange_partner_id_receiving_hours_credit_approved(self):
        result = super(SaleOrder, self).onchange_partner_id()
        values = {}
        if self.partner_id and self.partner_id.res_receiving_hours_id and self.partner_id.res_receiving_day_id.id:
            values['res_receiving_hours_id'] = self.partner_id.res_receiving_hours_id.id
            values['res_receiving_day_id'] = self.partner_id.res_receiving_day_id.id
        else:
            values['res_receiving_hours_id'] = False
            values['res_receiving_day_id'] = False

        if self.partner_id and self.partner_id.credit_limit:
            values['credit_limit'] = self.partner_id.credit_limit
        else:
            values['credit_limit'] = False

        if values:
            self.update(values)
        return result

