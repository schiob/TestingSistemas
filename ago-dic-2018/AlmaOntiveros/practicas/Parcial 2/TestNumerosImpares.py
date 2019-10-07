import unittest
import NumerosImpares

class TestNumerosImpares (unittest.TestCase):
    def test_numeros(self):

#Caso de Prueba 1
        total=NumerosImpares.calc(6, -5)
        self.assertEqual(total, 5)

#Caso de Prueba 2
        total=NumerosImpares.calc(12, 15)
        self.assertEqual(total, 13)

#Caso de Prueba 3
        total=NumerosImpares.calc(12, 12)
        self.assertEqual(total, 0)

#Caso de Prueba 4
        total=NumerosImpares.calc(123, 321)
        self.assertEqual(total, 21756)

#Caso de Prueba 5
        total=NumerosImpares.calc(4321, 1234)
        self.assertEqual(total, 4284911)

#Caso de Prueba 6
        total=NumerosImpares.calc(-19289, 7853)
        self.assertEqual(total, -77593260)

if __name__=='__main__':
    unittest.main()