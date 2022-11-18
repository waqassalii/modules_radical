# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ClassTen(models.Model):
    _name = 'class.ten'
    _description = 'teacher records'

    state = fields.Selection(
        [('draft', 'draft'),
         ('confirmed', 'confirmed'),
         ('cancelled', 'Cancelled')], string="status", default='draft',tracking=True)
    gender = fields.Selection([('female', 'Female'),('male', 'Male')])
    name = fields.Char(string='Student Name', required=True)
    image = fields.Binary()
    phone = fields.Char('Phone')
    age = fields.Integer(string='Age')
    id_card = fields.Integer(string='CNIC')
    date = fields.Date(string='Date', default=fields.datetime.today())

