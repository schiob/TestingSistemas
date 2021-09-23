import unittest
import random
from practica2 import suma

class TestSuma(unittest.TestCase):
    def test_suma(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        resultado_real = suma(a, b)
        self.assertEqual(resultado_real, a + b)
        print('a = ' + str(a) + '\nb = ' + str(b) + '\na + b = ' + str((a + b)))

if __name__ == '__main__':
    unittest.main() 