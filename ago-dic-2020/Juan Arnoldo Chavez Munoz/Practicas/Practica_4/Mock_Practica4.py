from Practica_4 import calculating_average, read_csv
import unittest
from unittest import mock
from unittest.mock import Mock, mock_open, patch 

    
class Mockeando(unittest.TestCase):
    mocker2 = "usersFake.csv"
    @mock.patch("builtins.open", return_value = mocker2, autospec=True)
    def test_algoSad(self, mock_get):
        esperado = [{'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'}, {'usuario': 'Juan', 'correo': 'juan@hotmail.com', 'puntos': '75'}]
        real = read_csv()
        assert esperado == real
    

    @patch("builtins.open")
    def test_func1(self, mock_open):
        mock_var = "usersFake.csv"
        mock_open.return_value = mock_var
        esperada = [{'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'}, {'usuario': 'Juan', 'correo': 'juan@hotmail.com', 'puntos': '75'}]
        salida_real = read_csv()
        assert salida_real == esperada
        
        
    @patch("builtins.open")
    def test_mockoooo(self, mock_open):
        mock_var = Mock(return_value=[{'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'}, {'usuario': 'Juan', 'correo': 'juan@hotmail.com', 'puntos': '75'}])
        #mock_var. ('{'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'}, {'usuario': 'Juan', 'correo': 'juan@hotmail.com', 'puntos': '75'}')
        mock_open.return_value = mock_var
        esperada = [{'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'}, {'usuario': 'Juan', 'correo': 'juan@hotmail.com', 'puntos': '75'}]
        salida_real = read_csv()
        assert salida_real == esperada
        #raise AttributeError(salida_real)

    @patch("Practica_4.calculating_average")#el mock reemplaza esa funcion
    def test_algoooo(self, mock_input):
        mockero = [{'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'}, {'usuario': 'Juan', 'correo': 'juan@gmail.com', 'puntos': '75'},{'usuario': 'Juan', 'correo': 'juan@outlook.com', 'puntos': '75'}]
        mock_input.return_value = mockero
        esperada = [{'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'}, {'usuario': 'Juan', 'correo': 'juan@gmail.com', 'puntos': '75'},{'usuario': 'Juan', 'correo': 'juan@outlook.com', 'puntos': '75'}]
        real = calculating_average([])
        assert esperada == real


    def test_mocking_constant(mocker):
        mocker.patch('Practica_4.calculating_average', return_value=[{'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'}, {'usuario': 'Juan', 'correo': 'juan@gmail.com', 'puntos': '75'},{'usuario': 'Juan', 'correo': 'juan@outlook.com', 'puntos': '75'}])
        esp2 = [{'usuario': 'Tom', 'correo': 'tomas@hotmail.com', 'puntos': '85'}, {'usuario': 'Juan', 'correo': 'juan@gmail.com', 'puntos': '75'},{'usuario': 'Juan', 'correo': 'juan@outlook.com', 'puntos': '75'}]
        expected = """hotmail 85
                    gmail 75
                    outlook 75"""
        actual = calculating_average([])  
        assert esp2 == actual
  
if __name__ == "__main__":
    unittest.main()