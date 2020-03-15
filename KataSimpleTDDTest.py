from unittest import TestCase

from KataSimpleTDD import KataSimpleTDD

class KataSimpleTDDTest(TestCase):

    #Contar Número de elementos

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

    # Hallar el mínimo de elementos
    def test_minimo_string_vacio(self):
        self.assertEqual(KataSimpleTDD().minimo(""),0,"Mínimo de string vacío")

    def test_minimo_string_con_una_cadena(self):
        self.assertEqual(KataSimpleTDD().minimo("1"),1,"Mínimo de una cadena")
        self.assertEqual(KataSimpleTDD().minimo("2"), 2, "Mínimo de una cadena")

    def test_minimo_string_con_dos_numeros_cadena(self):
        self.assertEqual(KataSimpleTDD().minimo("5,3"),3,"Mínimo de una cadena con dos números")

    def test_minimo_string_con_N_numeros_cadena(self):
        self.assertEqual(KataSimpleTDD().minimo("5,9,4,10,80"),4,"Mínimo de una cadena con N números")

    # Hallar el máximo de elementos
    def test_maximo_string_vacio(self):
        self.assertEqual(KataSimpleTDD().maximo(""),0,"Maximo de string vacio")

    def test_maximo_string_con_una_cadena(self):
        self.assertEqual(KataSimpleTDD().maximo("1"),1,"Maximo de una cadena")
        self.assertEqual(KataSimpleTDD().maximo("2"),2,"Maximo de un numero")

    def test_maximo_string_con_dos_numeros(self):
        self.assertEqual(KataSimpleTDD().maximo("5,8"),8,"Maximo de dos numeros")

    def test_maximo_string_con_N_numeros(self):
        self.assertEqual(KataSimpleTDD().maximo("5,96,74,252,63,84,99,15"),252, "Maximo de N numeros")
        
    # Hallar el promedio de los elementos
    def test_promedio_string_vacio(self):
        self.assertEqual(KataSimpleTDD().promedio(""),0, "Promedio de string vacío")

    def test_promedio_string_con_una_cadena(self):
        self.assertEqual(KataSimpleTDD().promedio("1"), 1, "Promedio de string con una cadena")
        self.assertEqual(KataSimpleTDD().promedio("2"), 2, "Promedio de string con una cadena")

    def test_promedio_string_con_dos_numeros_cadena(self):
        self.assertEqual(KataSimpleTDD().promedio("2,4"),3, "Promedio de string con dos números")

    def test_promedio_string_con_N_numeros_cadena(self):
        self.assertEqual(KataSimpleTDD().promedio("4,6,8,13,20"),10.2, "Promedio de string con N números")

    #Entregar Resultado completo
    def test_entregar_resultado_completo(self):
        self.assertEqual(KataSimpleTDD().resultado("4,6,8,13,20"),[5,4,20,10.2], "Resultados con N números")