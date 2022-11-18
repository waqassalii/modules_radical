# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AdmissionForm(models.Model):
    _name = 'admission.form'
    _description = 'in this model we create admission form of students all the record of students available here'

    name = fields.Char(string="RO No.", default=lambda self: _('new'))
    date = fields.Date('Date', default=fields.Date.today())
    state = fields.Selection(
        [('draft', 'draft'),
         ('confirmed', 'confirmed'),
         ('cancelled', 'Cancelled')], string="status", default='draft',tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    student_name = fields.Char(string='Student Name', required=True)
    image = fields.Binary()
    phone = fields.Char('Phone')
    relegion = fields.Char('Relegion')
    nationality = fields.Char('Nationality')
    guardian_phone = fields.Char('Guardian Phone')
    age = fields.Integer(string='Age')
    birth_day = fields.Date('Birth Day')
    class_id = fields.Many2one('school.classes',string='Class')
    previous_class = fields.Integer(string='Previous Class')
    guardian = fields.Char(string='Guardian Name')
    guardian_occupation = fields.Char(string='Guardian Occupation')
    guardian_id_card = fields.Integer(string='Guardian CNIC')
    address = fields.Text('Address')

    admission_form_line = fields.One2many('admission.form.line', 'admission_id', string="Form Line", ondelete='cascade')

    def action_send_sms(self):
        if not self.phone:
            raise ValidationError('No phone number is available')
        message = 'Hello mr %s ' % self.name
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.phone, message)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url,
        }

    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_draft(self):
        self.state = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('name', _('new')) == _('new'):
            vals['name'] = self.env['ir.sequence'].next_by_code('admission.form') or _('new')
        rep = super(AdmissionForm, self).create(vals)
        return rep


class AdmissionFormLine(models.Model):
    _name = 'admission.form.line'

    admission_id = fields.Many2one('admission.form', ondelete='cascade')
    admission_fee = fields.Float('Total Admission Fee', digits=(16, 2))
    semester_fee = fields.Float('Semester Fee', digits=(16, 2))
    paid_fee = fields.Float('Paid Admission Fee', digits=(16, 2))
    balance_fee = fields.Float('Balance', digits=(16, 2))

