# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AllAdmissionReport(models.AbstractModel):
    # _name = 'report.ModuleName.Template_id'
    _name = 'report.radical_school.report_admission_form_view'
    _description = 'Get Pdf for all records.'

    @api.model
    def _get_report_values(self, docids, data=None):

        docs = self.env['admission.form'].browse(docids)
        for doc in docs:
            if not doc.age:
                message = "Age for the %s student is not set please write the age." % doc.student_name
                raise ValidationError(message)
        return {
            'docs': docs,
        }
