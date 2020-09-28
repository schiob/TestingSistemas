from Practica4 import extract_data, calcular_promedio_deCSV
from unittest import mock, TestCase

class TestPractica4Mocks(TestCase):

    mocks = { 'mockChio': [['hotmail.com', 85], 
                       ['hotmail.com', 75],     
                       ['gmail.com', 90], 
                       ['outlook.com', 74], 
                       ['gmail.com', 88], 
                       ['hotmail.com', 92]],

               'mockDos': [["proton.com",100],
                        ['proton.com', 90],
                        ['gmail.com', 90],
                        ['gmail.com',88]],
                
                'mockEmpty': []
            }


    @mock.patch("Practica4.extract_data", return_value = mocks['mockChio'], autospec = True)
    def testMOCK_output_chio(self, mock_get):
        esperado = {'hotmail.com': 84.0, 'gmail.com': 89.0, 'outlook.com': 74.0}
        real = calcular_promedio_deCSV("mock")

        assert esperado == real

    @mock.patch("Practica4.extract_data", return_value = mocks['mockDos'], autospec = True)
    def testMOCK_output_normal(self, mock_get):
        esperado = {'proton.com': 95.0, 'gmail.com': 89.0}
        real = calcular_promedio_deCSV("mock")

        assert esperado == real
    
    @mock.patch("Practica4.extract_data", return_value = mocks['mockEmpty'], autospec = True)
    def testMOCK_output_empty(self, mock_get):
        esperado = {}
        real = calcular_promedio_deCSV("mock")

        assert esperado == real
    
    def testMOCK_output_formatoIncorrecto(self):
         
         with mock.patch('Practica4.open') as mock_open:
            CSV= "user,a,n"

            mock_open.return_value.__enter__.return_value = CSV
            with self.assertRaises(ValueError):
                extract_data("mock")
