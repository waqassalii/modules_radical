# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AdmissionForm(models.Model):
    _name = 'teacher.teacher'
    _description = 'teacher records'

    state = fields.Selection(
        [('draft', 'draft'),
         ('confirmed', 'confirmed'),
         ('cancelled', 'Cancelled')], string="status", default='draft',tracking=True)
    name = fields.Char(string='Teacher Name', required=True)
    image = fields.Binary()
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')])
    phone = fields.Char('Phone')
    age = fields.Integer(string='Age')
    id_card = fields.Integer(string='CNIC')
    class_id = fields.Many2one('school.classes',string='Class')
    date = fields.Date('Date', default=fields.Date.today())

    def get_admission_data(self):
        admission_record = self.env['admission.form'].search([])
        return admission_record

