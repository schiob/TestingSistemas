import unittest
import tracemalloc
from unittest import TestCase
from unittest.mock import patch
from promedio import calc_prom


tracemalloc.start()
class TestsPromedio(TestCase):
    @patch('builtins.open', create = True)
    def test1(self, mock_open):
        #mock_open.return_value = 
        esperado = 3
        self.assertEqual(calc_prom(), esperado)

if __name__ == '__main__':
    unittest.main()
