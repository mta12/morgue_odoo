from odoo.tests.common import TransactionCase
from datetime import date, timedelta


class TestEnregMort(TransactionCase):

    def setUp_past(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        self.Cadavre = self.env['morgue_cmr.cadavre']
        self.cadav = self.Cadavre.create({
            'nom_complet': 'Milika Dieu donné',
            'sexe': 'Masculin',
            'date_decces': date.today() + timedelta(-1),
            'date_enreg': date.today(),
            # On suppose par défaut c 10jrs
            'date_sortie': date.today+timedelta(10)
        })
        return result

    # Tester aussi les accès du user
    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)

        user_admin = self.env.ref('base.user_admin')
        self.env = self.env(user=user_admin)

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
        print("BONJOUR A TOUS")
        self.assertEqual(self.cadav.date_enreg, date.today())

    def test_check_barcode(self):
        "Vérifie que le numéro de dode est toujours valide"
        self.assertTrue(self.cadav._check_barcode)
