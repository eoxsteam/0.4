# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    pass_oil = fields.Char(string="Dry/Coil")

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def change_value(self):
        self.action_view_invoice = 'new value'

