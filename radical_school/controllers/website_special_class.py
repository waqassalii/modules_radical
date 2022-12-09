# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

# http.request.render['radical_website.teacher_form_template_id'
# if u want to write request.render then import
# from odoo.http import request


class SpecialClassController(http.Controller):
    @http.route('/special-class', auth='public', type='http', website=True)
    def special_class_form(self, **kw):
        print('/special-class method.........', kw)
        return http.request.render('radical_school.special_class_templ1', {})


class SpecialClassThanks(http.Controller):
    @http.route('/create/special-class', auth='public', type='http', website=True)
    def special_class_thanks(self, **kw):
        print('/create/special-class method')
        request.env['special.class'].sudo().create(kw)
        return request.render('radical_school.special_class_thanks', {})
