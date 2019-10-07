import unittest
import contar

class TestContar(unittest.TestCase):

    def test_contar(self):
        res=contar.calcular([2,3,-4,7,5])
        self.assertEqual(res[0], 2)
        self.assertEqual(res[1], 3)
        self.assertEqual(res[2], 4)
        self.assertEqual(res[3], 1)

if __name__ == '__main__':
    unittest.main()
