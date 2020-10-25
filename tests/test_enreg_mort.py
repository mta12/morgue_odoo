from odoo.tests.common import TransactionCase
from datetime import date, timedelta


class TestEnregCadavre(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        self.Cadavre = self.env['morgue_cmr.cadavre']
        self.cadav = self.Cadavre.create({
            'nom_prenom': 'Milika Dieu donné',
            'sexe': 'Masculin',
            'date_decces': date.today() + timedelta(-1),
            'date_enreg': date.today(),
            # On suppose par défaut c 10jrs
            'date_sortie': date.today+timedelta(10)
        })

        return result

    def test_create(self):
        "Test si l'enregistrement du cadavre est actuel"
        self.assertEqual(self.cadav.date_enreg, date.today())
