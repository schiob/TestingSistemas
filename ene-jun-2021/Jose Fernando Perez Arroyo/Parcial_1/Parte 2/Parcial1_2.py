import unittest

from Parcial1_1 import get_info, promediacion

class TestGetData(unittest.TestCase):
    def setUp(self):
        self.entrada_archivocsv = 'parcial.csv'
    
    def test_conseguirdatos(self):
        salida_esperada = get_info(self.entrada_parcialcsv)
        salida_real = [['hotmail.com', 85], ['hotmail.com', 75], ['gmail.com', 90], ['outlook.com', 74], ['gmail.com', 88], ['hotmail.com', 92]]
        self.assertEqual(salida_real, salida_esperada)

    def test_separacionypromediacion(self):
        salida_esperada = promediacion()
        salida_real = [['hotmail.com', 84.0], ['gmail.com', 89.0], ['outlook.com', 74.0]]
        self.assertEqual(salida_real, salida_esperada)

    def tearDown(self):
        del(self.entrada_archivocsv)

if __name__ == '__main__':
    unittest.main()