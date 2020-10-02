import unittest
from unittest.mock import patch, MagicMock
from internet import say_hi, MessageCreator

class MessageCreatorMock(MessageCreator):

    def CreateMessage(self, user: str) -> str:
        return "test message"


class TestAPI(unittest.TestCase):
    @patch("requests.get")
    def test_api(self, mock_get):
        test_cases = (
            {
                "entrada": "Erick",
                "mensaje_api": "This is Fucking Awesome. - Erick",
                "salida_esperada": "La API me contestó este bonito mensaje: This is Fucking Awesome. - Erick",
                "error_api": False,
            },
            {
                "entrada": "Erick",
                "mensaje_api": "",
                "salida_esperada": "error :(",
                "error_api": True,
            },
        )

        for cp in test_cases:
            if cp["error_api"]:
                mock_get.side_effect = Exception("error feo")
            else:
                respuesta_get = MagicMock()
                respuesta_get.text = cp["mensaje_api"]
                mock_get.return_value = respuesta_get


            salida_real = say_hi(cp["entrada"])

            headers = {"Accept": "application/json"}
            mock_get.assert_called_with("https://foaas.com/awesome/{}".format(cp["entrada"]), headers=headers)
            self.assertEqual(salida_real, cp["salida_esperada"])
        

if __name__ == "__main__":
    unittest.main()