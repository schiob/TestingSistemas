import unittest
import Correo_csv
from unittest.mock import patch

class correos_test(unittest.TestCase):
    @patch('request.post')

    def test_shout(self, mock_post):
                        #entrada-salida
        test_cases = (("usuario,correo,puntos"
                    "Tom,tomas@hotmail.com,85"
                    "Juan,juan@hotmail.com,75"
                    "Maria,maria84@gmail.com,90"
                    "Paco,paquito123@outlook.com,74"
                    "Ana,anaa22@gmail.com,88"
                    "Marcos,marcosss@hotmail.com,92", "hotmail.com 84.0\n"
                                                    "gmail.com 126.0\n"
                                                    "outlook.com 74.0\n"))

        for entrada, esperado in test_cases:

            salida_real = Correo_csv.puntos(entrada)
            self.assertEqual(salida_real, esperado)


if __name__ == '__main__':
    unittest.main()
