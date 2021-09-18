import unittest
from lista_numeros import lista_de_numeros

class testListaNumeros(unittest.TestCase):
    
    def numeros_positivos_test(self):
         test = lista_de_numeros([1, 2, 3, 4]);
         self.assertEqual(test, 'numero(s) positivo(s): 4\nnumero(s) negativo(s): 0\nnumero(s) par(es): 2\nnumero(s) impar(es): 2')
    
    def numeros_negativos_test(self):
         test = lista_de_numeros([-5, -4, -3, -1]);
         self.assertEqual(test, 'numero(s) positivo(s): 0\nnumero(s) negativo(s): 4\nnumero(s) par(es): 1\nnumero(s) impar(es): 3')
    
    def numeros_pares_test(self):
         test = lista_de_numeros([2, 4, 6, -2]);
         self.assertEqual(test, 'numero(s) positivo(s): 3\nnumero(s) negativo(s): 1\nnumero(s) par(es): 4\nnumero(s) impar(es): 0')
    
    def numeros_impares_test(self):
         test = lista_de_numeros([3, -5, -3, -7]);
         self.assertEqual(test, 'numero(s) positivo(s): 1\nnumero(s) negativo(s): 3\nnumero(s) par(es): 0\nnumero(s) impar(es): 4')
    
    def numeros_aleatorios_test(self):
         test = lista_de_numeros([5, -4, -2, 3, -1/2]);
         self.assertEqual(test, 'numero(s) positivo(s): 2\nnumero(s) negativo(s): 3\nnumero(s) par(es): 3\nnumero(s) impar(es): 2')
         

if __name__ == '__main__':
    unittest.main()