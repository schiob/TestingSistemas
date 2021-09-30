import unittest
from  unittest.mock import mock_open, patch
from practica4 import calc_prom

class TestPractica4(unittest.TestCase):
    @patch('builtins.open', mock_open(read_data='10\n20\n30'))
    def test_open_file_1(self):
        string_read = calc_prom()
        self.assertEqual(string_read, 60)
        open.assert_called_with('archivito.txt', 'r')

    @patch('builtins.open', mock_open(read_data='10\n20\n30\n10'))
    def test_open_file_2(self):
        string_read = calc_prom()
        self.assertEqual(string_read, 70)
        open.assert_called_with('archivito.txt', 'r')

    @patch('builtins.open', mock_open(read_data=''))
    def test_open_file_3(self):
        string_read = calc_prom()
        self.assertEqual(string_read, 0)
        open.assert_called_with('archivito.txt', 'r')
    
    @patch('builtins.open', mock_open(read_data='refe'))
    def test_open_file_4(self):
        self.assertRaises(Exception, calc_prom, 'refe')

if __name__ == '__main__':
    unittest.main()