# *-* coding:utf-8 -*-
"""."""
from odoo import fields
from odoo import models
from odoo.addons.ng_church.models.helper import parish


class ChurchProgram(models.Model):
    """ChurchService."""

    _name = 'ng_church.program'

    name = fields.Char('Name', required=True)
    days = fields.Selection([('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                             ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'),
                             ('Sunday', 'Sunday')], string='Day', default='Monday', required = True)
    start = fields.Float(string='Start Time')
    start_meridiem = fields.Selection([('AM', 'AM'), ('PM', 'PM')],string='')
    end = fields.Float(string='End Time')
    end_meridiem = fields.Selection([('AM', 'AM'), ('PM', 'PM')],string='')
    # meridiem = fields.Selection([('AM', 'AM'), ('PM', 'PM'), ('AM', 'PM'), ('PM', 'AM')], string='')
    parish_id = fields.Many2one('res.company', string='Parish', default=parish)
