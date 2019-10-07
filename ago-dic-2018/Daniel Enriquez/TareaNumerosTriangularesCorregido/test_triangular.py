import unittest
import triangular

class TestDan(unittest.TestCase):

    def test_triangular(self):
        resultado=triangular.convertir([1,3,4,56,400])

        self.assertEqual(resultado [0],1)#verifica que el numero triangular de 1 sea 1
        self.assertEqual(resultado [1],6)#verfica que el numero triangular de 3 sea 6
        self.assertEqual(resultado [2],10)#verifica que el numero triangular de 4 sea 10
        self.assertEqual(resultado [3],1596)#verifica que el numero troiangular de 56 sea 1596
        self.assertEqual(resultado [4],80200)#verifica que el numero triangular de 400 sea 80200

if __name__ == "__main__":
    unittest.main()
