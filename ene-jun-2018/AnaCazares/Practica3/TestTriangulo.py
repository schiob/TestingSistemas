import unittest
from triangulo import lado

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		self.lista=[1,2,3]

	#Funciones test:
    def test_equilatero(self):
        result = lista(3, 3, 3)
        self.assertEqual(result, 'Equilatero')
    def test_isosceles(self):
        result = lista(3, 3, 2)
        self.assertEqual(result, 'Isósceles')
    def test_escaleno(self):
        result = lista(2, 3, 4)
        self.assertEqual(result, 'Escaleno')
    def test_false(self):
        result = lista(1, 2, 3)
        self.assertEqual(result, 'No es rectangulo')
		
if __name__ == '__main__':
	unittest.main()
