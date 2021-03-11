
import unittest
from ejercicio1 import total

#class TestTotal(unittest.TestCase):
  #  def test_Total(self):
 #       pruebas = (
#
   #           ["cachete tripitas", 22],   
  #            ["lengua pastor", 25]
 #       )
#
   #     for prueba in pruebas:
  #          self.assertEqual(total(prueba[0], prueba[1]))

class Test_total(unittest.TestCase):

    def Test_Total1(self):
        resultado = total("cachete tripitas ")
        self.assertEqua(resultado, 22)

    def Test_Total2(self):
        resultado = total("cerdo tripitas ")
        self.assertEqua(resultado, 9)

    def Test_Total4(self):
        resultado = total("cachete tripitas pastor ")
        self.assertEqua(resultado, 37)


if __name__ == '__main__':
    unittest.main()