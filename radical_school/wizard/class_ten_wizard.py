# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClassTenWizard(models.TransientModel):
    """ Wizard allowing to grant a badge to a user"""
    _name = 'class.ten.wizard'
    _description = 'ten class wizard'

    gender = fields.Selection([('female', 'Female'), ('male', 'Male')])

    def action_print_class_ten(self):
        print('action is calling')
        domain = []
        if self.gender:
            domain += [('gender', '=', self.gender)]
        class_ten = self.env['class.ten'].search_read(domain)
        data = {
            'form_data' : self.read()[0],
            'class_ten' : class_ten,
        }
        return self.env.ref('radical_school.action_report_class_ten').report_action(self, data=data)


