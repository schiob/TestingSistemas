from typing import Text
import unittest
import builtins
from unittest import result, TestCase, mock
from unittest.mock import patch, mock_open
from textwrap import dedent
from parcial2 import leer_calificaciones
class leercalificaciones_test(unittest.TestCase):
    DATA = dedent("""Jose_Lopez quimica 89.00
Jose_Lopez matematicas 85.34
Maria_Martinez fisica 95.50

        """).strip()
    @patch("builtins.open", mock_open(read_data=DATA))
    def test_uno (self):
        with open("calificaciones", "r") as f:
                       result=f.read()
                       open.assert_called_once_with("calificaciones", "r")
        self.assertEqual(leer_calificaciones(),"""Jose_Lopez 87.17
Maria_Martinez 95.5""")


if __name__ =='__main__':
 unittest.main()