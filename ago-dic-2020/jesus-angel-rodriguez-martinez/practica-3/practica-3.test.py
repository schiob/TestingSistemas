import unittest

from practica import vender_pantalones

class VenderPantalonesTest(unittest.TestCase):
    def test_base_case_for_selling_pants(self):
        n = 8
        x = 5
        lista_pantalones_ordenada = ['Nike 20', 'Nike 18', 'Levice 15', 'Patito 5', 'Patito 5', 'Patito 4', 'Levice 4', 'Levice 3']
        self.assertEqual(vender_pantalones(lista_pantalones_ordenada, n, x), "3 40")
    
    def test_making_a_good_sale(self):
        n = 8
        x = 5
        lista_pantalones_ordenada = ['Nike 200', 'Levice 100', 'Levice 80', 'Patito 5', 'Patito 4', 'Levice 4']
        self.assertEqual(vender_pantalones(lista_pantalones_ordenada, n, x), "3 185")

    def test_selling_less_pants_than_the_goal(self):
        n = 5
        x = 2
        lista_pantalones_ordenada = ['Nike 20', 'Levice 15', 'Patito 5', 'Patito 4', 'Levice 3']
        self.assertEqual(vender_pantalones(lista_pantalones_ordenada, n, x), "0")

    def test_selling_more_than_five_pants(self):
        n = 10
        x = 2
        lista_pantalones_ordenada = ['Nike 20', 'Nike 20', 'Nike 20', 'Nike 20', 'Nike 20', 'Nike 20', 'Levice 15', 'Patito 5', 'Patito 4', 'Levice 3']
        self.assertEqual(vender_pantalones(lista_pantalones_ordenada, n, x), "0")

    def test_not_being_able_to_sell_pants(self):
        n = 3
        x = 1
        lista_pantalones_ordenada = ['Nike 20', 'Levice 15', 'Patito 5']
        self.assertEqual(vender_pantalones(lista_pantalones_ordenada, n, x), "0")

if __name__ == "__main__":
    unittest.main()
