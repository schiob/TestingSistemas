import unittest
from suma import sumaNumeros

class TestSumar(unittest.TestCase):
    
    def test_suma_enteros(self):
        resultado = sumaNumeros(5, 10)
        self.assertEqual(resultado, 15)
    
    def test_suma_negativos(self):
        resultado = sumaNumeros(-10, -5)
        self.assertEqual(resultado, -15)
    
    def test_suma_decimales(self):
        resultado = sumaNumeros(10.5, 5.5)
        self.assertEqual(resultado, 16)
    
    def test_suma_decimales_negativos(self):
        resultado = sumaNumeros(-10.5, -5.5)
        self.assertEqual(resultado, -16)
    
    def test_suma_dif_signos(self):
        resultado = sumaNumeros(-10, 10)
        self.assertEqual(resultado, 0)
    
    def test_suma_ceros(self):
        resultado = sumaNumeros(0, 0)
        self.assertEqual(resultado, 0)
    
    def test_suma_letras(self):
        resultado = sumaNumeros('A', 'B')
        self.assertEqual(resultado, 'AB')
    
    def test_suma_fracciones(self):
        resultado = sumaNumeros(1/2, 1/6)
        self.assertEqual(resultado, 4/6)
    
if __name__ == '__main__':
    unittest.main()
        