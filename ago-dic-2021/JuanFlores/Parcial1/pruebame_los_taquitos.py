import unittest
from taquitos import pedido

class TestTaquitosMethods(unittest.TestCase):

    def test_suma(self):
        total = pedido('cachete lengua cachete tripitas machito machito machito cachete lengua')
        self.assertEqual(total, 110)
    def test_cinco_de_tripita(self):
        total = pedido('tripitas tripitas tripitas tripitas tripitas')
        self.assertEqual(total, 45)
    def test_uno_de_cada_uno(self):
        total = pedido('cachete lengua tripitas pastor machito')
        self.assertEqual(total, 61)

if __name__ == '__main__':
    unittest.main()