# -*- coding: utf-8 -*-
# from odoo import http


# class RadicalSchool(http.Controller):
#     @http.route('/radical_school/radical_school/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/radical_school/radical_school/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('radical_school.listing', {
#             'root': '/radical_school/radical_school',
#             'objects': http.request.env['radical_school.radical_school'].search([]),
#         })

#     @http.route('/radical_school/radical_school/objects/<model("radical_school.radical_school"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('radical_school.object', {
#             'object': obj
#         })
