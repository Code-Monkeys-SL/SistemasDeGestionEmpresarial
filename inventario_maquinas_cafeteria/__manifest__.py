# -*- coding: utf-8 -*-
{
    'name': "InventarioMaquinasCafeteria",

    'summary': "Gestión de inventario de maquinas de la cafeteria",

    'description': """
Este es un modulo que va a servir para inventariar las maquinas que tiene la cafeteria y llevar un control de sus mantenimientos.
    """,

    'author': "Code_Monkeys",
    'website': "https://www.codemonkeys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Indicaremos que es una aplicación
    'aplication': True,
}

