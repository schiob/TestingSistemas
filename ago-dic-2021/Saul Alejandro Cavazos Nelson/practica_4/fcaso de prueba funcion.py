from os import error
from unittest import TestCase, result
from unittest import mock
from unittest.mock import patch
from funcion import calc_prom
import unittest
class test_parte_1(unittest.TestCase):
    @patch ("builtins.open")
    #@unittest.expectedFailure
    def test_1(self,muck_open):
        pruebas =[["1",1],["00000000",0],["54678",30],["",0]]
        for i in range(0,len(pruebas),1):
            muck_open.return_value=pruebas[i][0]
            saliad=pruebas[i][1]
            self.assertEqual(calc_prom(),saliad)


    @patch ("builtins.open")
    @unittest.expectedFailure
    def test_(self,muck_open):
        pruebas =[[" ",0],["123e",1],["hola",0],["hola\nhola",0]]
        for i in range(0,len(pruebas),1):
            muck_open.return_value=pruebas[i][0]
            saliad=pruebas[i][1]
            self.assertEqual(calc_prom(),saliad)


if __name__ =='__main__':
 unittest.main()