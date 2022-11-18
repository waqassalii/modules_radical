# -*- coding: utf-8 -*-
from odoo import http


# to pass the data from model to controller
class RadicalTeacherController(http.Controller):
    @http.route('/radical/teachers/', auth='public', website=True)
    def passing_admission_form_data(self, **kw):
        teacher_forms = http.request.env['teacher.teacher'].search([])
        return http.request.render('radical_website.teacher_form_template_id', {'teacher_forms': teacher_forms})

    @http.route('/radical/teacher/<int:id>', auth='public', website=True)
    def display_student_id(self, id):
        teacher_form = http.request.env['teacher.teacher'].browse([id])
        return http.request.render('radical_website.teacher_form_single_template_id', {'teacher_form': teacher_form})

