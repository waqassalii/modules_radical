# -*- coding: utf-8 -*-
# from odoo import http


# class RadicalWebsite(http.Controller):
#     @http.route('/radical_website/radical_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/radical_website/radical_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('radical_website.listing', {
#             'root': '/radical_website/radical_website',
#             'objects': http.request.env['radical_website.radical_website'].search([]),
#         })

#     @http.route('/radical_website/radical_website/objects/<model("radical_website.radical_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('radical_website.object', {
#             'object': obj
#         })
