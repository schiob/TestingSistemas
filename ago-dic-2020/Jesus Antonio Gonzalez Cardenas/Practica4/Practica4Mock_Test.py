from Practica4 import getAverages
import unittest
import unittest.mock
from unittest.mock import patch,MagicMock

class csvTest(unittest.TestCase):
    def test1(self):
        mock_csv = MagicMock()
        testdict = {'hotmail.com': 81.33, 'protonmail.com': 88.33}


