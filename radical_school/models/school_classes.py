# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SchoolClasses(models.Model):
    _name = 'school.classes'
    _description = 'School classes Records'

    state = fields.Selection(
        [('draft', 'draft'),
         ('confirmed', 'confirmed'),
         ('cancel', 'Cancelled')], string="status", default='draft',tracking=True)
    name = fields.Char(string='Student Name', required=True)
    image = fields.Binary()


