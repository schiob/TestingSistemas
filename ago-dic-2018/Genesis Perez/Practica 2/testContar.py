import unittest
import contar

class TestContar (unittest.TestCase):
    def test_clasifica(self):
        res=contar.clasif([3])
        self.assertEqual(res[0], 1) #positivo
        self.assertEqual(res[1], 0) #negativo
        self.assertEqual(res[2], 0) #par
        self.assertEqual(res[3], 1) #impar

if __name__ == '__main__':
    unittest.main()
