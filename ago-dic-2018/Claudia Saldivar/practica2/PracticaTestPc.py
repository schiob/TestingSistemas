import unittest
import PracticaenPc

class TestJuanita(unittest.TestCase):
    def test_numeros(self):
        res=PracticaenPc.calc([0,4,3,5,8])
        self.assertEqual(res[1],2)

if __name__=='__main__':
    unittest.main()
