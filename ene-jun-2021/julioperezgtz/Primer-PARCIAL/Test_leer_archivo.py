import unittest 
from unittest.mock import *
from leer_archivo import *

class Test_archivo(unittest.Testcase):
    @patch('builtinis.open', new_callable=mock_open, read_data="Tom,tomas@hotmail.com,85\nMaria,maria84@gmail.com,90\nPaco,paquito123@outlook.com,74\nAna,anaa22@gmail.com,88\nMarcos,marcosss@hotmail.com,92")
    def testarchivo(self, mock_file):
        self.assertEqual(abrir(mock_file),'hotmail.com 84.0\ngmail.com 89.0\noutlook.com 74.0')