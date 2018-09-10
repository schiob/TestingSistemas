
import unittest
import PracticaenPc

class TestJuanita(unittest.TestCase):
    def test_numeros(self):

        res = PracticaenPc.calc(4,[1,2,3,4])
        self.assertEqual(resultado[0], 4)
        self.assertEqual(resultado[1], 0)
        self.assertEqual(resultado[2], 2)
        self.assertEqual(resultado[3], 2)

        res = PracticaenPc.calc(5,[1,3,7,-4,-2])
        self.assertEqual(resultado[0], 3)
        self.assertEqual(resultado[1], 2)
        self.assertEqual(resultado[2], 2)
        self.assertEqual(resultado[3], 3)
        self.assertEqual(resultado[4], 5)

        res = PracticaenPc.calc(3,[-2,2,3])
        self.assertEqual(resultado[0], 2)
        self.assertEqual(resultado[1], 1)
        self.assertEqual(resultado[2], 2)

if __name__=='__main__':
    unittest.main()
