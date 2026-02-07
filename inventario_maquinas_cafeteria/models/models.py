# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class maquina(models.Model):
    _name = 'inventario_maquinas_cafeteria.maquina'
    _description = 'Permite definir de las maquinas de la cafeteria'
    _order = 'cod'

    cod = fields.Integer(string='Codigo', required=True, help='Codigo de la maquina definido internamente en la cafeteria para identificarlas')
    name = fields.Char('Nombre', required=True)
    ubicacion = fields.Char('Ubicación')
    adquirido = fields.Date(string='Fecha de adquisición')
    estado = fields.Selection(string='Estado', selection=[('s', 'Sin estrenar'), ('o', 'Operativa'), ('r', 'Rota')], default='s')
    coste = fields.Float('Coste', (4, 1), default=0.0, help='Coste de compra de la maquina')

    tiempo_adquirido = fields.Integer(string='Tiempo desde adquisición (días)', compute='_calcular_tiempo_adquirido')

    # relacciones entre tablas
    mantenimiento_ids = fields.One2many('inventario_maquinas_cafeteria.mantenimiento', 'maquina_id', string='Mantenimientos')

    @api.depends('adquirido')
    def _calcular_tiempo_adquirido(self):
        for record in self:
            if record.adquirido:
                fecha_adquirido = fields.Date.from_string(record.adquirido)
                result = (datetime.today().date() - fecha_adquirido).days
                record.tiempo_adquirido = result
            else:
                record.tiempo_adquirido = 0

class mantenimiento(models.Model):
    _name = 'inventario_maquinas_cafeteria.mantenimiento'
    _description = 'Permite definir los mantenimientos de las maquinas dela cafeteria'

    descripcion = fields.Char(string='Descripción', required=True)
    tecnico = fields.Char(string='Técnico', required=True)
    coste = fields.Float('Coste', (10, 2), default=0.0, help='Coste de realizar el mantenimiento', required=True)
    fecha = fields.Date(string='Fecha de realización del mantenimiento')

    # Relaciones entre tablas
    maquina_id = fields.Many2one('inventario_maquinas_cafeteria.maquina', string='Máquina')

