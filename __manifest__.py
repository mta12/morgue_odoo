# -*- coding: utf-8 -*-
{
    'name': "Hos-Morgue",

    'summary': """
        Module de gestion d'une Morgue d'hopital""",

    'description': """
        Gestion de la Morgue: 
        - gestion des défunts et de leurs responsables 
        - gestion des coffrets pour cadavres
        - gestion des opérations financières y associées
        - Etablissement des bilans financiers
    """,

    'author': "Powered by MTA (Manga Tobie A.)",
    'website': "https://github.com/mta12/morgue_odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Mortuary',
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
    'application': True,
}
