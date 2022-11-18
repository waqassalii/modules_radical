# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ClassStudents(models.Model):
    _name = 'class.students'
    _description = 'School classes Records'

    state = fields.Selection(
        [('draft', 'draft'),
         ('confirmed', 'confirmed'),
         ('cancel', 'Cancelled')], string="status", default='draft',tracking=True)
    class_id = fields.Many2one('school.classes', string='Class')

    class_students_line = fields.One2many('class.students.line', 'class_student_id', string='Students',
                                          store=True, ondelete='cascade')

    def dell_rec(self):
        for rec in self:
            rec.class_students_line = [(5,0,0)]

    @api.onchange('class_id')
    def list_of_students_in_class(self):
        admissions = self.env['admission.form'].search([('class_id', '=', self.class_id.id)])
        o2m_list = []
        if admissions:
            for admission in admissions:
                o2m_list.append((0,0,{
                   'student_name': admission.student_name,
                   'gender': admission.gender,
                   'age': admission.age,
                   'class_name': admission.class_id.name,
                   'class_student_id': self.id,
                }))
        self.class_students_line = False
        self.class_students_line = o2m_list
        # self.update({
        #     'class_students_line': o2m_list
        # })


class ClassStudentsLine(models.Model):
    _name = 'class.students.line'

    class_student_id = fields.Many2one('class.students')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    student_name = fields.Char(string='Student Name')
    class_name = fields.Char(string='Class')
    age = fields.Integer(string='Age')


