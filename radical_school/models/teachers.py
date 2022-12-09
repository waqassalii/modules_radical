# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

from odoo.tools import date_utils


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
    plus_date = fields.Date('Plus Date')
    start_quarter = fields.Date('Start quarter')
    end_quarter = fields.Date('End quarter')
    year = fields.Char(default=lambda self: fields.Date.today().year)
    # quarter = fields.Selection([
    #     ('1', '1st'),
    #     ('2', '2nd'),
    #     ('3', '3rd'),
    #     ('4', '4th'),
    # ], required=True, default=lambda self: str(date_utils.get_quarter_number(fields.Date.today())))
    note = fields.Html('Description', compute="_compute_description_default_value")

    def get_admission_data(self):
        admission_record = self.env['admission.form'].search([])
        return admission_record

    def action_get_month(self):
        today = fields.Datetime.today()
        rec_date = self.date
        for rec in self:
            quater = date_utils.get_quarter(self.date)
            print(quater, 'quater')

    @api.depends('note')
    def _compute_description_default_value(self):
        self.note ="hello im your wrost enemy"

        # self.note = '<iframe src="https://www.youtube.com/watch?v=Z3O3ntxWOHA" style="height:50%;width:50%"></iframe>'

    # @api.depends('year', 'quarter')
    # def _compute_dates(self):
    #     for dmfa in self:
    #         year = int(dmfa.year)
    #         month = int(dmfa.quarter) * 3
    #         self.quarter_start, self.quarter_end = date_utils.get_quarter(date(year, month, 1))

    # / home / aljamoos / odoo14 / odoo / enterprise / l10n_be_hr_payroll / models / hr_dmfa.py

