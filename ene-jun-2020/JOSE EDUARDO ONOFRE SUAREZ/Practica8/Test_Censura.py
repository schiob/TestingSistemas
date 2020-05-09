import unittest
from Censura import censura
from Validacion import validacion
from unittest.mock import MagicMock

class testValCensura(unittest.TestCase):

    def esValida(self):
        testcases = [
            {
                "nombre": "La diferencia es menor al limite",
                "censurar_mock_res" : "la sonic tiene mucha sonic",
                "entrada": 5,
                "salida_esperada": "El texto sigue siendo valido",

            }

        

        ]

        for tc in testcases:

            censura_mock = MagicMock()
            censura_mock.censurar_mock_res.return_value = tc["censurar_mock_res"]
            
            self.assertEqual(validacion.validar(),)


