from calificaciones import calcular_promedio
import unittest
from unittest import TestCase
from mock import patch, MagicMock

alumnos = ['juan_cedillo quimica 89.00', 'juan_cedillo matematicas 85.34', 'mariana_martinez fisica 95.50', 'mariana_martinez espanol 90.00']
class Test(unittest.TestCase):
    @patch('builtins.open')
    def testPromedio(self, mock_open):
        for x in range(len(alumnos)):
            mock_open.return_value.read.return_value = alumnos[x]
            get = calcular_promedio(mock_open)
            resultado = calcular_promedio(alumnos)
            self.assertEqual(get, resultado)


if __name__ == '__main__':
    unittest.main()