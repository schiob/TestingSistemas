import unittest
from practica2 import write_file, read_file

class TestReadWrite(unittest.TestCase):

    # Tests 1-3: Se aseguran de que el contenido del archivo coincida con el 2do parámetro.

    def test_1(self):
        self.assertEqual(read_file('print1.txt'), 'hola tacos')

    def test_2(self):
        self.assertEqual(read_file('print2.txt'), '')

    def test_3(self):
        self.assertEqual(read_file('print3.txt'), 'hola\nsalto\ntamal')

    # Tests 4-5: Comparan el contenido de dos archivos y aseguran que coincida.

    def test_4(self):
        self.assertEqual(read_file('lizard.txt'), read_file('t4.txt'))

    def test_5(self):
        self.assertEqual(read_file('friday.txt'), read_file('t5.txt'))


if __name__ == '__main__':
    unittest.main()
