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

    def test_contar_conDosNumeros(self):
        self.assertEqual(KataSimpleTDD().contar("1,2"), 2,"Dos numeros")

    def test_contar_conMultiplesNumeros(self):
        self.assertEqual(KataSimpleTDD().contar("1,5,9,3,4"), 5,"Multiples numeros")

    def test_minimo_string_vacio(self):
        self.assertEqual(KataSimpleTDD().minimo(""),0,"Mínimo de string vacío")

    def test_minimo_string_con_una_cadena(self):
        self.assertEqual(KataSimpleTDD().minimo("1"),1,"Mínimo de una cadena")
        self.assertEqual(KataSimpleTDD().contar("2"), 2, "Mínimo de una cadena")