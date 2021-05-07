import unittest
import requests
from unittest.mock import patch, MagicMock
from mayusc import Conversor
class Modulo_de_pruebas_unitarias(unittest.TestCase):

    @patch('requests.post')
    def pruebas_unitarias_coversor_a_mayus(self, mock_post):
        
        mock = MagicMock()

        tc = (
            ["jaja saludos equisdee", """{ "INPUT":"jaja saludos equisdee","OUTPUT":"JAJA SALUDOS EQUISDEE" }"""],
            ["Si jalo el test?", """{ "INPUT":"Si jalo el test?","OUTPUT":"SI JALO EL TEST?" }"""],
            ["456", """{ "INPUT":"456","OUTPUT":"456" }"""],
            ["no se que mas probar...", """{ "INPUT":"no se que mas probar...","OUTPUT":"NO SE QUE MAS PROBAR..." }"""]
        )

        for i in tc:
            
            mock.text = Conversor.conversor_a_mayusculas(1)
            mock_post.return_value = mock

            self.assertEquals(Conversor.conversor_a_mayusculas(0), Conversor.conversor_a_mayusculas(1))

    @patch('os.path.isfile')
    @patch('file.read')
    def pruebas_unitarias_validador_de_existencia(self):
        pass

    def pruebas_unitarias_funcion_principal(self):
        pass

    def pruebas_integrales(self):
        pass

if __name__ == "__main__":
    unittest.main()