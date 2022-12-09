# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SpecialClass(models.Model):
    _name = 'special.class'
    _description = 'Special class students'

    name = fields.Char(string='Teacher Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')])
    phone = fields.Char('Phone')


