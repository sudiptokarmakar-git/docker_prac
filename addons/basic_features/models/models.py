# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class basic_features(models.Model):
#     _name = 'basic_features.basic_features'
#     _description = 'basic_features.basic_features'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

