# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AdmissionForm(models.Model):
    _name = 'duplicate.admission.form'
    _inherits = {'admission.form': 'admission_id'}
    _description = 'in this model we create admission form of students all the record of students available here'

    admission_id = fields.Many2one('admission.form', string='Admission Form')

    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_draft(self):
        self.state = 'draft'


class AdmissionFormLine(models.Model):
    _name = 'duplicate.admission.form.line'
#     _inherits = {'admission.form.line': 'admission_line_id'}
#
#     duplicate_admission_id = fields.Many2one('duplicate.admission.form', ondelete='cascade')
#     admission_line_id = fields.Many2one('admission.form.line', ondelete='cascade')
