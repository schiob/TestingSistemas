import unittest
from sumar import suma_dos_numeros

class sumar_test(unittest.TestCase):

    def test_suma_enteros(self):
        resultado = suma_dos_numeros(5, 8)
        self.assertEqual(resultado, 13)

    def test_suma_enteros_negativos(self):
        resultado = suma_dos_numeros(-5, -3)
        self.assertEqual(resultado, -8)

    def test_suma_flotantes(self):
        resultado = suma_dos_numeros(0.5, 0.25)
        self.assertEqual(resultado, 0.75)

    def test_suma_enteros_signos_diferentes(self):
        resultado = suma_dos_numeros(10, -12)
        self.assertEqual(resultado, -2)

    def test_suma_ceros(self):
        resultado = suma_dos_numeros(0, 0)
        self.assertEqual(resultado, 0)

    def test_suma_fracciones(self):
        resultado = suma_dos_numeros(1/2, 1/3)
        self.assertEqual("{:.2f}".format(resultado), "{:.2f}".format(5/6))

if __name__ == '__main__':
    unittest.main()
