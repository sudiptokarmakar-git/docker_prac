# -*- coding: utf-8 -*-
# from odoo import http


# class BasicFeatures(http.Controller):
#     @http.route('/basic_features/basic_features', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/basic_features/basic_features/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('basic_features.listing', {
#             'root': '/basic_features/basic_features',
#             'objects': http.request.env['basic_features.basic_features'].search([]),
#         })

#     @http.route('/basic_features/basic_features/objects/<model("basic_features.basic_features"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('basic_features.object', {
#             'object': obj
#         })

