from unittest import TestCase

from KataSimpleTDD import KataSimpleTDD

class KataSimpleTDDTest(TestCase):
    def test_contar(self):
        self.assertEqual(KataSimpleTDD().contar(""), 0,"Cadena vacia")
        
    def test_contar_unacadena(self):
        self.assertEqual(KataSimpleTDD().contar("1"), 1,"Un numero")

    def test_contar_cadenaConUnNumero(self):
        self.assertEqual(KataSimpleTDD().contar("1"), 1,"Un numero")
        self.assertEqual(KataSimpleTDD().contar("2"), 1,"Un numero")