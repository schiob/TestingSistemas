import unittest
import calificaciones
from unittest.mock import patch

def Funcion_mock(self):
    return 'Prueba'

class test(unittest.TestCase):
    @patch('builtins.open')
    def test_mock(self,mock_open):
        mock_open.return_value.read.return_value = '''
        Jose_Lopez quimica 89.00 
        Jose_Lopez matematicas 85.34
        '''
        arch=calificaciones.materias_alumno('Prueba1_Parcial2.txt')
        self.assertEqual(arch,'Jose_Lopez 87.17'
        ) 

    def test_mock2(self,mock_open):
        mock_open.return_value.read.return_value = '''
        Maria_Martinez fisica 95.50
        Maria_Martinez español 90.00
        '''
        arch=calificaciones.materias_alumno('Prueba1_Parcial2.txt')
        self.assertEqual(arch,'Maria_Martinez 92.75'
        ) 

if __name__ == "__main__":
	unittest.main()