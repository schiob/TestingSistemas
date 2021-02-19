import unittest
from Triangulo import tipo_triangulo

class PruebasFunciones(unittest.TestCase):

    def test_Equi(self):
        self.assertEqual(tipo_triangulo(9, 9, 9), 'Equilatero')
    def test_Esca(self):
        self.assertEqual(tipo_triangulo(7, 8, 10), 'Escaleno')
    def test_Isos(self):
        self.assertEqual(tipo_triangulo(7, 7, 9), 'Isósceles')
    def test_muygrande(self):
        self.assertEqual(tipo_triangulo(7, 7, 9999999999999999999), 'Los lados del triangulo no pueden ser tan grandes')
    def test_NungunTR(self):
        self.assertEqual(tipo_triangulo(-7, 7, 10), 'No es ningun triángulo, no se permiten numeros negativos o 0')   
    def test_Letras(self):
        self.assertEqual(tipo_triangulo("p", 7, 10), 'No triangulo')     
if __name__ == '__main__':
    unittest.main()