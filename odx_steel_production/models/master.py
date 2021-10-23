from odoo import models, fields, exceptions, api


class ProductionMachine(models.Model):
    _name = 'production.machine'

    machine_code = fields.Char(string="Machine Code")
    name = fields.Char(string="Machine Name")
