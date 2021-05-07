import unittest
from unittest.mock import patch, MagicMock
import Parcial2 as p2

class Tests(unittest.TestCase):
    #Unit Tests
    def test_Funcion1Existe(self):
        path = "prueba1.txt"
        resultadoEsperado = "asdf"
        resultado = p2.get_Contenido(path)
        self.assertEqual(resultado, resultadoEsperado)
    def test_Funcion1NoExiste(self):
        path = "prueba100.txt"
        cadena = "El archivito no estaba pero mientras ve este bonito perrito:\n... el perrito se escapo!!!\n"
        resultado = p2.get_Contenido(path)
        self.assertEqual(resultado, cadena)

    def test_Funcion2ConTexto(self):
        texto = "holi a todos"
        resultadoEsperado = "HOLI A TODOS"
        resultadoReal = p2.Shouter(texto)
        self.assertEqual(resultadoReal, resultadoEsperado)
    def test_Funcion2SinTexto(self):
        texto = ""
        resultadoEsperado = "No hay texto"
        resultadoReal = p2.Shouter(texto)
        self.assertEqual(resultadoReal, resultadoEsperado)
    
    #Integration Test (Bottom-Up)
    @patch("Parcial2.Shouter")
    def test_Con_Mock(self, mock_response):
        mock_response.return_value = "ASDF"
        resultadoReal = p2.Mezcla("prueba1.txt")
        self.assertEqual(resultadoReal, "asdf, ASDF")

    @patch("Parcial2.Shouter")
    def test_Con_Mock2(self, mock_response):
        mock_response.return_value = "No hay texto"
        resultadoReal = p2.Mezcla("prueba100.txt")
        self.assertEqual(resultadoReal, "El archivito no estaba pero mientras ve este bonito perrito:\n... el perrito se escapo!!!\n")

    @patch("Parcial2.Shouter")
    def test_Con_Mock3(self, mock_response):
        mock_response.return_value = "No hay texto"
        resultadoReal = p2.Mezcla("prueba2.txt")
        self.assertEqual(resultadoReal, "No hay texto")

if __name__  == "__main__":
    unittest.main()