# -*- coding: utf-8 -*-
# from odoo import http


# class InventarioMaquinasCafeteria(http.Controller):
#     @http.route('/inventario_maquinas_cafeteria/inventario_maquinas_cafeteria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventario_maquinas_cafeteria/inventario_maquinas_cafeteria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventario_maquinas_cafeteria.listing', {
#             'root': '/inventario_maquinas_cafeteria/inventario_maquinas_cafeteria',
#             'objects': http.request.env['inventario_maquinas_cafeteria.inventario_maquinas_cafeteria'].search([]),
#         })

#     @http.route('/inventario_maquinas_cafeteria/inventario_maquinas_cafeteria/objects/<model("inventario_maquinas_cafeteria.inventario_maquinas_cafeteria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventario_maquinas_cafeteria.object', {
#             'object': obj
#         })

