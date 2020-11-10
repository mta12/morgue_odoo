# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Cadavre(models.Model):
    _name = 'morgue_cmr.cadavre'
    _description = 'The Deceased'

    nom_complet = fields.Char('Nom du décedé')
    sexe = fields.Char('Sexe')

    date_enreng = fields.Date()
    date_sortie = fields.Date()
    date_deces = fields.Date()

    actif = fields.Boolean('est actif?', default=True)

    responsable = fields.Many2many(
        'res.partner', string='Responsable du corps')

    etat_corps = fields.Text('Etat du corps')
