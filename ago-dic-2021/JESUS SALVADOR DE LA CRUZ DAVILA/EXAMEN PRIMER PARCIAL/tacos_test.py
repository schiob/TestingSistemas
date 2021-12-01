import unittest

from tacos import *

class TestTacos(unittest.TestCase):
    
    def test_solo_tacos_de_cachete(self):
        test = lista_de_tacos(['cachete', 'cachete', 'cachete', 'cachete', 'cachete'])
        self.assertEqual(test, 65)
    
    def test_solo_tacos_de_lengua(self):
        test = lista_de_tacos(['lengua', 'lengua', 'lengua', 'lengua', 'lengua'])
        self.assertEqual(test, 50)
    
    def test_solo_tacos_de_tripitas(self):
        test = lista_de_tacos(['tripitas', 'tripitas', 'tripitas', 'tripitas', 'tripitas'])
        self.assertEqual(test, 45)
    
    def test_solo_tacos_de_pastor(self):
        test = lista_de_tacos(['pastor', 'pastor', 'pastor', 'pastor', 'pastor'])
        self.assertEqual(test, 75)
    
    def test_solo_tacos_de_machito(self):
        test = lista_de_tacos(['machito', 'machito', 'machito', 'machito', 'machito'])
        self.assertEqual(test, 70)
    
    def test_tacos_de_al_pastor_que_no_existe(self):
        test = lista_de_tacos(['machito', 'machito', 'alpastor', 'alpastor', 'alpastor'])
        self.assertEqual(test, 28)
    
    def test_lista_vacia(self):
        test = lista_de_tacos([''])
        self.assertEqual(test, 0)
    


if __name__ == '__main__':
    unittest.main()