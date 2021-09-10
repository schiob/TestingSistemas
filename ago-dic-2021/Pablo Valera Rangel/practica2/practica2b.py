import unittest
from practica2a import sumaNumeros


class TestIgualdad(unittest.TestCase):

    def testDosNumerosIguales(self):
        resultadoReal = sumaNumeros(3, 5)
        self.assertEqual(resultadoReal, 8)

    def testDosNumerosDiferentes(self):
        resultadoReal = sumaNumeros(5, -3)
        self.assertEqual(resultadoReal, 2)

    def testPosUnoNeg(self):
        resultadoReal = sumaNumeros(7, -10)
        self.assertEqual(resultadoReal, -3)

    def testNegPos(self):
        resultadoReal = sumaNumeros(-6, 11)
        self.assertEqual(resultadoReal, 5)
    
    def testDosNegativos(self):
        resultadoReal = sumaNumeros(-6, -13)
        self.assertEqual(resultadoReal, -19)
        
    def testDosCeros(self):
        resultadoReal = sumaNumeros(0, 0)
        self.assertEqual(resultadoReal, 0)
    
    def testErroneo(self):
        resultadoReal = sumaNumeros(10, 13)
        self.assertNotEqual(resultadoReal, -19)
    
    def testVerdadero(self):
        resultadoReal = sumaNumeros(10, 13)
        self.assertTrue(23)

if __name__ == '__main__':
    unittest.main()
