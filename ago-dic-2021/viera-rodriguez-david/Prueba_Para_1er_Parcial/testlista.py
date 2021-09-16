import unittest
from ejeprueba import lectura_tabla 

class casos(unittest.TestCase):
    def test1(self):
       resultado_esperado="2 Numero(s) Positivo(s)\n""2 Numero(s) Negativo(s)\n""3 Numero(s) Par(es)\n""2 Numero(s) Impar(es)\n"
       self.assertEqual(lectura_tabla(5,"51 -12 -3 0 2"),resultado_esperado)

    def test2(self):
       resultado_esperado="4 Numero(s) Positivo(s)\n""0 Numero(s) Negativo(s)\n""3 Numero(s) Par(es)\n""2 Numero(s) Impar(es)\n"
       self.assertEqual(lectura_tabla(5 ,"0 1 2 3 4"),resultado_esperado)

    def test3(self):
       resultado_esperado="0 Numero(s) Positivo(s)\n""3 Numero(s) Negativo(s)\n""1 Numero(s) Par(es)\n""2 Numero(s) Impar(es)\n"
       self.assertEqual(lectura_tabla(3,"-1 -2 -3"),resultado_esperado)

    def test4(self):
       resultado_esperado="0 Numero(s) Positivo(s)\n""0 Numero(s) Negativo(s)\n""1 Numero(s) Par(es)\n""0 Numero(s) Impar(es)\n"
       self.assertEqual(lectura_tabla(1,"0"),resultado_esperado)
if __name__ == '__main__':
    unittest.main()