import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_negatiivinen(self):
        self.varasto = Varasto(-1)

    def test_alkusaldo_negatiivinen(self):
        self.varasto = Varasto(10, -1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisataan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-1)
    
    def test_lisataan_liikaa(self):
        maara = self.varasto.paljonko_mahtuu() + 1
        self.varasto.lisaa_varastoon(maara)

    def test_otetaan_negatiivinen_maara(self):
        self.varasto.ota_varastosta(-1)

    def test_otetaan_liikaa(self):
        maara = self.varasto.saldo + 1
        self.varasto.ota_varastosta(maara)

    def test_tulostus_oikei(self):
        saldo = Varasto(6)

        self.assertEqual(str(saldo), "saldo = 0, vielä tilaa 6")
        

