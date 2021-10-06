import unittest
import tracemalloc
from unittest import TestCase
from unittest.mock import patch
from practica4_doc import cp

tracemalloc.start()
class TestsPromedio(TestCase):
    @patch('__main__.open', create = True)
    def test1(self, mock_open):
        mock_open.return_value = 3
        esperado = 3
        self.assertEqual(cp(), esperado)

if __name__ == '__main__':
    unittest.main()