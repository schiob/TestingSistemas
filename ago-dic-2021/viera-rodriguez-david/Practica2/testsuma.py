import unittest
from practica2 import suma_dos_numeros

class testsuma(unittest.TestCase):
    def test_enteros(self):
        resultado = suma_dos_numeros(5, 6)
        self.assertEqual(resultado, 11)

    def test_enteronegativo(self):
        resultado = suma_dos_numeros(5, -6)
        self.assertEqual(resultado, -1)

    def test_negativos(self):
        resultado = suma_dos_numeros(-5, -3)
        self.assertEqual(resultado, -8)
    
    def test_decimales(self):
        resultado = suma_dos_numeros(0.5, 1.6)
        self.assertEqual(resultado, 2.1)
    
    def test_decimalesnegativo(self):
        resultado = suma_dos_numeros(-0.4, -0.5)
        self.assertEqual(resultado, -0.9)

    def test_fracciones(self):
        resultado = suma_dos_numeros(3/5, 3/4)
        self.assertEqual(resultado, 27/20)
    
    def test_fraccionesneg(self):
        resultado = suma_dos_numeros(-1/2, -1/2)
        self.assertEqual(resultado, -1)

    def test_ceros(self):
        resultado = suma_dos_numeros(0, 0)
        self.assertEqual(resultado, 0)
    
    def test_letras(self):
        resultado = suma_dos_numeros(g, 6)
        self.assertEqual(resultado, "error")
    
    def test_letras2(self):
        resultado = suma_dos_numeros(6, h)
        self.assertEqual(resultado, "error")
    
    def test_fraccionesceros(self):
        resultado = suma_dos_numeros(0/0, 0/0)
        self.assertEqual(resultado, "error")

    

    

if __name__ == '__main__':
    unittest.main()