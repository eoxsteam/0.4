from odoo import models, fields, exceptions, api


class ProductionMachine(models.Model):
    _name = 'production.machine'

    machine_code = fields.Char(string="Machine Code")
    name = fields.Char(string="Machine Name")
    machine_scheduler_ids = fields.One2many('machine.scheduler', 'machine_id', string="Machine Scheduler")


class MachineScheduler(models.Model):
    _name = 'machine.scheduler'
    _order = 'sequence asc'

    start_time = fields.Datetime(string="Start Time")
    sequence = fields.Integer(string='Sequence', default=10)
    end_time = fields.Datetime(string="End Time")
    work_order_id = fields.Many2one('production.instructions', string="Work order")
    pr_run_id = fields.Many2one('instructions.run.line', string="Prod. Run",
                                domain="[('prod_inst_ref_id', '=', work_order_id) or [] ] ")
    machine_id = fields.Many2one('production.machine', string="Machine Id")
