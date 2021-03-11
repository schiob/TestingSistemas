import unittest
from numeros import Check_Num

class TestNumeros(unittest.TestCase):
    def test_numeros1(self):

        resultado = Check_Num("s l n o p")
        self.assertEqual(resultado, "Error digitaste una letra")

    def test_numeros2(self):

        resultado = Check_Num(5 4 18 20 0)
        self.assertEqual(resultado, (0, "número(s) negativo(s)\n", 4," número(s) positivos(s)\n",3," número(s) par(es)\n", 2," número(s) impar(es)\n",1,"número(s) neutro(s)"))

if __name__ == "__main__":    
    unittest.main()