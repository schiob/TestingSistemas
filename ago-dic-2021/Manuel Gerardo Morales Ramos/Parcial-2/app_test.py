import unittest
import unittest.mock as mock
from unittest.mock import patch

from app import get_students_average, domain

test_cases = [
            {
                'name': 'Case 1 ok',
                'input': 'Carla_Valdes probabilidad 70.00\nCarla_Valdes español 94.34\nCarla_Valdes geografia 85.00\nEstefanía_Gonzales calculo 85.00\nEstefanía_Gonzales fisica 76.50\nEstefanía_Gonzales quimica 89.49\nTomas_Ordaz programación 70.00\nTomas_Ordaz etica 97.60\nTomas_Ordaz redes 97.60\nJose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34',
                'expected_output': {'Carla_Valdes': 83.11333333333333, 'Estefanía_Gonzales': 83.66333333333334, 'Tomas_Ordaz': 88.39999999999999, 'Jose_Lopez': 87.17},
                'expected_raise': False,
            },
            {
                'name': 'Case 2 error',
                'input': '',
                'expected_output': {'Carla_Valdes': 83.11333333333333, 'Estefanía_Gonzales': 83.66333333333334, 'Tomas_Ordaz': 88.39999999999999, 'Jose_Lopez': 87.17},
                'expected_raise': True,
            },
    ]
class TestParcial2(unittest.TestCase):
    @patch('mocks.File.Read')
    def test_archivito(self, mock_file_read):
        for test in test_cases:
            mock_file_read.return_value = test['input']
            
            if test["expected_raise"]:
                self.assertRaises(Exception, get_students_average)
            else:
                result = get_students_average()
                self.assertEqual(test['expected_output'], result)
    
    # Top/Down
    @patch('app.add_student')
    @patch('app.get_students_average')
    def test_domain(self, mock_get_students_average, mock_add_student):
        mock_get_students_average.return_value = {'Carla_Valdes': 83.11333333333333, 'Estefanía_Gonzales': 83.66333333333334, 'Tomas_Ordaz': 88.39999999999999, 'Jose_Lopez': 87.17}
        mock_add_student.return_value = 'Victor_Valdes probabilidad 70.00'
        self.assertEqual(domain(), True)

if __name__ == '__main__':
    unittest.main()
