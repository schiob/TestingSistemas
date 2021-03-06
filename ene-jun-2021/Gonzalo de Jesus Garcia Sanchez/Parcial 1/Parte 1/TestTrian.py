import unittest
from NumerosTriangulares import NumTriang as x

class TestNumero(unittest.TestCase):
    def test_tipo(self):
        test =       [((1),1),
                      ((3),6),
                      ((4),10),
                      ((56),1596),
                      ((400),80200)]
        for lista, esperado in test:
            actual = x(lista)
            self.assertEqual(esperado,actual)
if __name__ == '__main__':
    unittest.main()