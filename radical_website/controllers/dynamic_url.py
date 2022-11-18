# -*- coding: utf-8 -*-
from odoo import http

# by website=true it will be supported by website
# following one is the static url


class RadicalDynamicWebsite(http.Controller):
    @http.route('/radical/student', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"

# url for string may be chracter or integer
    @http.route('/radical/student/<name>', auth='public', website=True)
    def display_every_student_rec(self, name):
        return "<h1>hellow '<b>{}</b>'</h1>".format(name)

    # if you pass in radical/student/tashi the page would return as hellow tashi

    # to make it to get integer value only you should write like following
    # it won't accept string parameter
    @http.route('/radical_student/<int:id>', auth='public', website=True)
    def display_student_id(self, id):
        return "<h1>this is the id = '<b>{}</b>' </h1>".format(id)
        # return "<h1>this is the id = '<b>{}</b>' </h1>".format(type(id).__name__)

    # odoo provides dynamic url method which is model
    # just like the above method in place of int write model and instead of id write any variable name
    # dont forget to pass the variable in parameters and in dictionary along with template id
    @http.route('/radical/teacher/<model("teacher.teacher"):variable>/', auth='public', website=True)
    def display_model_student_id(self, variable):
        return http.request.render['radical_website.teacher_form_template_id', {'key of variable': variable}]
