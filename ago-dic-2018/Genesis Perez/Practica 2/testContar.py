import unittest
import contar

class TestContar (unittest.TestCase):
    def test_clasifica(self):
        # Caso de prueba 1
        res=contar.clasif([0, 25, -0])
        self.assertEqual(res[0], 1) #positivo
        self.assertEqual(res[1], 1) #negativo
        self.assertEqual(res[2], 2) #par
        self.assertEqual(res[3], 1) #impar
        # Caso de prueba 2
        res=contar.clasif([0, 25, -0])
        self.assertEqual(res[0], 1) #positivo
        self.assertEqual(res[1], 0) #negativo
        self.assertEqual(res[2], 2) #par
        self.assertEqual(res[3], 1) #impar
        # Caso de prueba 3
        res=contar.clasif([-15, -1, 15, 1])
        self.assertEqual(res[0], 2) #positivo
        self.assertEqual(res[1], 2) #negativo
        self.assertEqual(res[2], 0) #par
        self.assertEqual(res[3], 4) #impar
        # Caso de prueba 4
        res=contar.clasif([3])
        self.assertEqual(res[0], 1) #positivo
        self.assertEqual(res[1], 0) #negativo
        self.assertEqual(res[2], 0) #par
        self.assertEqual(res[3], 1) #impar
        
if __name__ == '__main__':
    unittest.main()
