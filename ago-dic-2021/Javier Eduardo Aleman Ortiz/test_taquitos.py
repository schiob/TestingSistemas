import unittest
from taquitos import tacos
class test_tacos(unittest.TestCase):
    def test_una_unidad(self):
        orden=tacos(('cachete',))
        
        self.assertEqual(orden, 13)

    def test_diez_unidades(self):
        orden=tacos(('cachete','lengua','tripitas','cachete','machito','machito','machito','cachete','lengua','cachete'))

        self.assertEqual(orden, 123)
    
    def test_cero_unidades(self):
        orden=tacos(())

        self.assertEqual(orden, 0)
    
    def test_trinta_unidades(self):
        orden=tacos(('cachete','lengua','tripitas','cachete','machito','machito','machito','cachete','lengua','cachete',
        'cachete','lengua','tripitas','cachete','machito','machito','machito','cachete','lengua','cachete',
        'cachete','lengua','tripitas','cachete','machito','machito','machito','cachete','lengua','cachete'))

        self.assertEqual(orden, 369)

    def test_mas_de_treinta_unidades(self):
        orden=tacos(('cachete','lengua','tripitas','cachete','machito','machito','machito','cachete','lengua','cachete',
        'cachete','lengua','tripitas','cachete','machito','machito','machito','cachete','lengua','cachete',
        'cachete','lengua','tripitas','cachete','machito','machito','machito','cachete','lengua','cachete','cachete'))

        self.assertEqual(orden, "orden no debe exeder las 30 unidades")

if __name__=="__main__":
    unittest.main()

