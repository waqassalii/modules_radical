# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request



class RadicalResumeController(http.Controller):
    @http.route('/resumes', auth='public', type='http', website=True)
    def resumes_submit_form(self, **kw):
        if not kw.get('applicant_name'):
            return request.render("radical_school.radical_resume_templ1",{})

        if kw.get('applicant_name'):
            resume_dict = {
                'name': kw['applicant_name'],
                'age': kw['applicant_age'] if kw.get('applicant_gender') else"23",
                'gender': kw['applicant_gender'] if kw.get('applicant_gender') else"male",
                'phone': kw['applicant_phone'] if kw.get('applicant_phone') else"12345678",
                'id_card': kw['applicant_id_card'] if kw.get('applicant_id_card') else"12345678",
                'education': kw['applicant_qualification'],
            }
            request.env['radical.resume'].sudo().create(resume_dict)
            return request.render("radical_school.radical_resumes_thanks", {})


    #     print('/special-class method.........', kw)
    #     return http.request.render('radical_school.special_class_templ1', {})



