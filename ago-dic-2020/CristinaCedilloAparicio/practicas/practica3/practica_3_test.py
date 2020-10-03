import unittest
from practica_3 import pantalones

class TestPractica(unittest.TestCase):
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
        entrada_3=["Levice","Wrangler"]
        entrada_4=[8,10]
        salida_esperada=None
        salida_real=pantalones(entrada_1,entrada_2,entrada_3,entrada_4)
        self.assertEqual(salida_real,salida_esperada)
    
    def test_upper3(self):
        entrada_1=14
        entrada_2=8
        entrada_3=['Patito','Patito','Levice','Patito','Levice','Nike','Nike','Levice','Wrangler','Ariat','CK','Ariat','Wrangler','Ariat']
        entrada_4=[4,5,15,5,3,20,18,4,15,20,8,14,25,25]
        salida_esperada=(6, 110)
        salida_real=pantalones(entrada_1,entrada_2,entrada_3,entrada_4)
        self.assertEqual(salida_real,salida_esperada)
     
   

if __name__=="__main__":
    unittest.main()
    