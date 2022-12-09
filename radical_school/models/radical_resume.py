# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

from odoo.tools import date_utils


class RadicalResume(models.Model):
    _name = 'radical.resume'
    _description = 'Resumes are recorded here'

    name = fields.Char(string='Teacher Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')])
    phone = fields.Char('Phone')
    id_card = fields.Integer(string='CNIC')
    education = fields.Char('Qualifications')
