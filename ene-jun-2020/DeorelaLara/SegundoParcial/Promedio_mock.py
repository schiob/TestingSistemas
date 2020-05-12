import promedio
import unittest
from unittest import *

Alumnos = ['Jose_Lopez quimica 89.00', 'Jose_Lopez matematicas 85.34', 'Maria_Martinez fisica 95.50', 'Maria_Martinez espaÃ±ol 90.00']

class Test(unittest.TestCase):
    @patch('builtins.open')
    def testPromedio(self, mock_open):
        for x in range(len(Alumnos)):
            mock_open.return_value.read.return_value = Alumnos[x]
            get = Promedio(mock_open)
            resultado = Promedio(splt)
            self.assertEqual(get, resultado)


if __name__ == '__main__':
    unittest.main()
