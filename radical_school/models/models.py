# -*- coding: utf-8 -*-

from odoo import models, fields, api


class radical_school(models.Model):
    _name = 'radical_school.radical_school'
    _description = 'radical_school.radical_school'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            if record.value:
                record.value2 = float(record.value) / 100
            else:
                record.value2 = 0.0
