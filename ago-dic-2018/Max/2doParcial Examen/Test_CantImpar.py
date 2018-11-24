import unittest
from CantImpares import cantImpar

class Test_Cantidad(unittest.TestCase):
    def test_Cantidad_Prueba(self):
        res = cantImpar(6, -5)
        self.assertEqual(res, 5)

    def test_Cantidad_Prueba(self):
        res = cantImpar(12, 15)
        self.assertEqual(res, 13)

    def test_Cantidad_Prueba(self):
        res = cantImpar(12, 12)
        self.assertEqual(res, 0)

    def test_Cantidad_Prueba(self):
        res = cantImpar(123, 321)
        self.assertEqual(res, 4284911)

    def test_Cantidad_Prueba(self):
        res = cantImpar(-19289, 7853)
        self.assertEqual(res, -77593260)

if __name__ == '__main__':
	unittest.main()
