import unittest
import triangular

class TestDan(unittest.TestCase):

    def test_triangular(self):
        resultado=triangular.convertir([1,3,4,56,400])

        self.assertEqual(resultado [0],1)
        self.assertEqual(resultado [1],6)
        self.assertEqual(resultado [2],10)
        self.assertEqual(resultado [3],1596)
        self.assertEqual(resultado [4],80200)

if __name__ == "__main__":
    unittest.main()
