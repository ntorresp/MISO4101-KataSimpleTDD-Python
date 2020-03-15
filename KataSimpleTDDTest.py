from unittest import TestCase

from KataSimpleTDD import KataSimpleTDD

class KataSimpleTDDTest(TestCase):
    def test_contar(self):
        self.assertEqual(KataSimpleTDD().contar(""),0,"Cadena vacia")
