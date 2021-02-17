import unittest
from practica1 import contador as conta

class TestP1(unittest.TestCase):
    ### solo para tener algo que hacer commit
    def test3p3i3pos3neg(self):
        linea = "3 3 3 -2 -2 -2"
        a = conta(linea)
        self.assertEqual(a,(3," numero(s) positivo(s).\n",3," numero(s) negativo(s).\n",3," numero(s) par(es).\n",3," numero(s) impar(es)."))
    
    def testAllCeros(self):
        linea = "0 0 0 0 0 0"
        a = conta(linea)
        self.assertEqual(a,(0," numero(s) positivo(s).\n",0," numero(s) negativo(s).\n",6," numero(s) par(es).\n",0," numero(s) impar(es)."))

    def testNonLegalInput(self):
        linea = "a a a a a"
        a = conta(linea)
        self.assertEqual(a,"Introduzca un número válido")

    def testMixedInputs(self):
        linea = "a 1 a 1 a 1"
        a = conta(linea)
        self.assertEqual(a, "Introduzca un número válido")

    def testDecimalInputs(self):
        linea = "1.1 2.2 3.3"
        a = conta(linea)
        self.assertEqual(a, "Introduzca un número válido")

if __name__ == '__main__':
    unittest.main()