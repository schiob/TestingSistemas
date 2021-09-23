import unittest
from unittest.main import main
from taquitos import taquitosClase

class testTacos(unittest.TestCase):
    def test1(self):
        '''ejemplo del prof'''
        lista = ["cachete", "lengua", "cachete", "tripitas", "machito", "machito", "machito", "cachete", "lengua"]
        entrada = taquitosClase(lista)
        self.assertEqual(entrada, 110)

    def test2(self):
        '''orden de lengua'''
        lista = ["lengua", "lengua", "lengua", "lengua", "lengua"]
        entrada = taquitosClase(lista)
        self.assertEqual(entrada, 50)

    def test3(self):
        '''sin hambre'''
        lista = ["pastor"]
        entrada = taquitosClase(lista)
        self.assertEqual(entrada, 15)

    def test4(self):
        '''con la novia (dos ordenes)'''
        lista = ["pastor", "pastor", "cachete", "tripitas", "machito", "machito", "machito", "cachete", "lengua", "pastor", "tripitas"]
        entrada = taquitosClase(lista)
        self.assertEqual(entrada, 141)

    def test5(self):
        '''uno de cada uno'''
        lista = ["cachete", "lengua", "tripitas", "pastor", "machito"]
        entrada = taquitosClase(lista)
        self.assertEqual(entrada, 61)
    

if __name__ == '__main__':
    unittest.main()
    