import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open
from Practica_4 import calc_prom

class test_Practica4(TestCase):

    @patch('builtins.open', mock_open(read_data='1\n2\n3'))

    def test_practica4_1(self):
        string_read = calc_prom()
        self.assertEqual(string_read, 6)
        open.assert_called_with('archivito.txt', 'r')

    @patch('builtins.open', mock_open(read_data='15\n25\n35\n45'))

    def test_practica4_2(self):
        string_read = calc_prom()
        self.assertEqual(string_read, 120)
        open.assert_called_with('archivito.txt', 'r')

    @patch('builtins.open', mock_open(read_data=''))

    def test_practica4_3(self):
        string_read = calc_prom()
        self.assertEqual(string_read, 0)
        open.assert_called_with('archivito.txt', 'r')


if __name__ == "__main__":
    unittest.main()
