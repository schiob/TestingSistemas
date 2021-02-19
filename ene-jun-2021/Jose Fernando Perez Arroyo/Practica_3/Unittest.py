import unittest
from Practica1 import pruebarara

class simpleunittest(unittest.TestCase):
    def test_practica2(self):
        la = 'as dad jkk jkkl'
        
        self.assertEqual(pruebarara(la), 'Error digitaste una letra')

    def test_practica1(self):
        l = '51 -12 -3 0 2'
    
        self.assertEqual(pruebarara(l), (2, "número(s) positivo(s)\n", 2," número(s) negativos(s)\n", 3," número(s) par(es)\n", 2," número(s) impar(es)"))
    

if __name__ == "__main__":
    unittest.main()


