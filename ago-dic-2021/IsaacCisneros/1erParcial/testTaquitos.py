import unittest
from  Taquitos import total

class Test_total(unittest.TestCase):

    def test_Total1(self):
        resultado = total(" barbacoa")
        self.assertEqual(resultado, 0)

    def test_Total2(self):
        resultado = total("tripitas cachete tripitas machito pastor")
        self.assertEqual(resultado, 61)

    def test_Total4(self):
        resultado = total(" cachete tripitas pastor ")
        self.assertNotEqual(resultado, 350)
    
    def test_Total5(self):
        resultado = total(" bistek ")
        self.assertNotEqual(resultado, 35)


if __name__ == '__main__':
    unittest.main() 