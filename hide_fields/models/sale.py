# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    state = fields.Selection([
            ('draft', 'Quote'),
            ('sent', 'Quote Sent'),
            ('sale', 'Sales Order'),
            ('done', 'Locked'),
            ('cancel', 'Cancelled'),
            ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
