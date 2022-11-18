# -*- coding: utf-8 -*-
from odoo import http


# to pass the data from model to controller
class RadicalWebsite(http.Controller):
    @http.route('/radical/admissions/', auth='public', website=True)
    def passing_admission_form_data(self, **kw):
        admission_forms = http.request.env['admission.form'].search([])
        return http.request.render('radical_website.admission_form_template_id', {'admissions': admission_forms})

    @http.route('/radical/admissions/<model("admission.form"):admission>/', auth='public', website=True)
    # @http.route('/radical/admission/', auth='public', website=True)
    # def display_single_form(self):
    def display_single_form(self, admission):
        return http.request.render('radical_website.admission_form_single_template_id', {'admission': admission})
        # if admission:
        #     return http.request.render['radical_website.admission_form_single_template_id', {'admission': admission}]
        # else:
        #     return "the is no any record of this  student"
