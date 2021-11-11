import unittest
from unittest import mock
from unittest.mock import mock_open, patch
import parcial2

class parte1(unittest.TestCase):

    def test_mock(self):
        
        calificaciones = """Adrian calculo 90.1
    Adrian programacion 100
    Pedro calculo 89.9
    Pedro programacion 83.1"""

        mock_1 = mock_open(read_data=calificaciones)

        resultado_esperado = ['Adrian 95.05', 'Pedro 86.5']

        with patch('builtins.open', mock_1):
            calculo = parcial2.leer_archivo()

        self.assertEqual(resultado_esperado, calculo)




if __name__ == '__main__':
    unittest.main() 