import unittest

from practica3 import lista
class test_suma(unittest.TestCase):
    def test_lista_1(self):
        test=lista((51,-12,-3,0,2))
        self.assertEqual(test,'Numeros positivos:\n2\nNumeros negativos:\n2\nNumeros pares:\n3\nNumeros impares:\n2')

    def test_lista_2(self):
        test=lista((0,1,2,3,4))
        self.assertEqual(test,'Numeros positivos:\n4\nNumeros negativos:\n0\nNumeros pares:\n3\nNumeros impares:\n2')

    def test_lista_3(self):
        test=lista((-1,-2,-3))
        self.assertEqual(test,'Numeros positivos:\n0\nNumeros negativos:\n3\nNumeros pares:\n1\nNumeros impares:\n2')

    def test_lista_4(self):
        test=lista((0,))
        self.assertEqual(test,'Numeros positivos:\n0\nNumeros negativos:\n0\nNumeros pares:\n1\nNumeros impares:\n0')
            
        
if __name__=="__main__":
    unittest.main()
