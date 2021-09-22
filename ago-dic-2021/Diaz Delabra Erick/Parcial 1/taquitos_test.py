import unittest
from unittest.main import main
from taquitos import taquitosClase

class testTacos(unittest.TestCase):
    def test1(self):
        lista = ["cachete", "lengua", "cachete", "tripitas", "machito", "machito", "machito", "cachete", "lengua"]
        entrada = taquitosClase(lista)
        self.assertEqual(entrada, 110)

if __name__ == '__main__':
    unittest.main()
    