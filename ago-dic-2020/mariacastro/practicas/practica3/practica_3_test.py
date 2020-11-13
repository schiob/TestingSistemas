import unittest
from practica_2 import pantalones

class TestPantalones(unittest.TestCase):

    def test_upper(self):
        entrada_1=8
        entrada_2=5
        entrada_3=['Patito','Patito','Levice','Patito','Levice','Nike','Nike','Levice']
        entrada_4=[4,5,15,5,3,20,18,4]
        salida_esperada=(3, 40)
        salida_real=pantalones(entrada_1,entrada_2,entrada_3,entrada_4)
        self.assertEqual(salida_real,salida_esperada)
    
    def test_upper2(self):
        entrada_1=2
        entrada_2=1
        entrada_3=["Levice","Patito"]
        entrada_4=[5,19]
        salida_esperada=None
        salida_real=pantalones(entrada_1,entrada_2,entrada_3,entrada_4)
        self.assertEqual(salida_real,salida_esperada)
    
    def test_upper3(self):
        entrada_1=5
        entrada_2=3
        entrada_3=['Levice','Levice','Levice','Levice','Levice']
        entrada_4=[10,3,7,11,4]
        salida_esperada=(2, 21)
        salida_real=pantalones(entrada_1,entrada_2,entrada_3,entrada_4)
        self.assertEqual(salida_real,salida_esperada)
     
   

if __name__=="__main__":
    unittest.main()
    