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

class PurchaseOrder(models.Model):
    _inherit= "purchase.order"

    rfq_date = fields.Datetime("RFQ Date")
    expected_due_date = fields.Datetime("Expected Due Date")
    is_hot = fields.Boolean("Hot")
    po_type_id = fields.Many2one("res.po.type",
                                 string="PO Type")

    @api.model
    def default_get(self, fields):
        res = super(PurchaseOrder, self).default_get(fields)
        po_type_obj = self.env['res.po.type'].search([("name","=","MAT")])
        if po_type_obj:
            res['po_type_id'] = po_type_obj.id
        return res
