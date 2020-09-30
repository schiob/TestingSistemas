import unittest
from unittest.mock import patch
from practica4 import conseguirdatos, separacionypromediacion

class TestGetData(unittest.TestCase):
    mocks = { 'ejemplo': [['hotmail.com', 85], 
                       ['hotmail.com', 75],     
                       ['gmail.com', 90], 
                       ['outlook.com', 74], 
                       ['gmail.com', 88], 
                       ['hotmail.com', 92]],

               'ejemplo2': [['zoho.com', 100],
                        ['proton.com', 92],
                        ['zoho.com', 91],
                        ['proton.com', 80],
                        ['zoho.com', 76]],

                'ejemplo3': [['tutanota.com', 80],
                        ['tutanota.com', 60],
                        ['gmx.com', 70],
                        ['newton.com', 90],
                        ['tutanota.com', 70],
                        ['gmx.com', 100],
                        ['newton.com', 90]],

                'ejemplo4': [['mail.com', 80],
                            ['mail.com', 92],
                            ['mail.com', 40],
                            ['mail.com', 70]]
            }
    
    @patch("practica4.conseguirdatos", return_value = mocks['ejemplo'])
    def test_separacionypromediacion(self, mock_get):
        salida_esperada = separacionypromediacion()
        salida_real = [['hotmail.com', 84.0], ['gmail.com', 89.0], ['outlook.com', 74.0]]

        self.assertEqual(salida_real, salida_esperada)
    
    @patch("practica4.conseguirdatos", return_value = mocks['ejemplo2'])
    def test_separacionypromediacion2(self, mock_get):
        salida_esperada = separacionypromediacion()
        salida_real = [['zoho.com', 89.0], ['proton.com', 86.0]]

        self.assertEqual(salida_real, salida_esperada)
    
    @patch("practica4.conseguirdatos", return_value = mocks['ejemplo3'])
    def test_separacionypromediacion3(self, mock_get):
        salida_esperada = separacionypromediacion()
        salida_real = [['tutanota.com', 70.0], ['gmx.com', 85.0], ['newton.com', 90.0]]

        self.assertEqual(salida_real, salida_esperada)
    
    @patch("practica4.conseguirdatos", return_value = mocks['ejemplo4'])
    def test_separacionypromediacion4(self, mock_get):
        salida_esperada = separacionypromediacion()
        salida_real = [['mail.com', 70.5]]

        self.assertEqual(salida_real, salida_esperada)

if __name__ == '__main__':
    unittest.main()
