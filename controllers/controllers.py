# -*- coding: utf-8 -*-
from odoo import http

# class MorgueCmr(http.Controller):
#     @http.route('/morgue_cmr/morgue_cmr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/morgue_cmr/morgue_cmr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('morgue_cmr.listing', {
#             'root': '/morgue_cmr/morgue_cmr',
#             'objects': http.request.env['morgue_cmr.morgue_cmr'].search([]),
#         })

#     @http.route('/morgue_cmr/morgue_cmr/objects/<model("morgue_cmr.morgue_cmr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('morgue_cmr.object', {
#             'object': obj
#         })