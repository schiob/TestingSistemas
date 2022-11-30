import unittest
from juanita import numeros

class TestJuanitaMethods(unittest.TestCase):
    def test_1(self):
        nums = "51 -12 -3 0 2"
        res = numeros(0, nums)
        test = "2 número(s) positivo(s)\n2 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"
        self.assertEqual(res, test)
    
    def test_2(self):
        nums = "0 1 2 3 4"
        res = numeros(0, nums)
        test = "4 número(s) positivo(s)\n0 número(s) negativo(s)\n3 número(s) par(es)\n2 número(s) impar(es)"
        self.assertEqual(res, test)
    
    def test_3(self):
        nums = "-1 -2 -3"
        res = numeros(0, nums)
        test = "0 número(s) positivo(s)\n3 número(s) negativo(s)\n1 número(s) par(es)\n2 número(s) impar(es)"
        self.assertEqual(res, test)
    
    def test_4(self):
        nums = "0"
        res = numeros(0, nums)
        test = "0 número(s) positivo(s)\n0 número(s) negativo(s)\n1 número(s) par(es)\n0 número(s) impar(es)"
        self.assertEqual(res, test)

if __name__ == '__main__':
    unittest.main()