import unittest
import mock
from Mock import leer_archivo as R
from Mock import AbrirArchivo as A
from Mock import Calif as C
from Mock import SortCalif as S
from Mock import Promedio as P

class TestPractica4(unittest.TestCase):
    #test normal
    def Test(self):
        archivo = A()
        self.assertEqual(archivo,[['usuario', 'correo', 'puntos'], ['Tom', 'tomas@hotmail.com', '85'], ['Juan', 'juan@hotmail.com', '75'], ['Maria', 'maria84@gmail.com', '90'], ['Paco', 'paquito123@outlook.com', '74'], ['Ana', 'anaa22@gmail.com', '88'], ['Marcos', 'marcosss@hotmail.com', '92']])
    
    # test mock
    def test_read_file(self):
        with mock.patch("builtins.open", mock.mock_open(read_data="MOCKED"), create=True) as mock_file:
            result = R("path")
        mock_file.assert_called_once_with("path", "r")
        assert result == "MOCKED"
    
    def test_CorreoCalif(self):
        lista = C([['usuario', 'correo', 'puntos'], ['Tom', 'tomas@aurom.com', '85'], ['Juan', 'juan@hotmail.com', '75'], ['Maria', 'maria84@gmail.com', '90'], ['Paco', 'paquito123@outlook.com', '74'], ['Ana', 'anaa22@gmail.com', '88'], ['Marcos', 'marcosss@hotmail.com', '92']]
    )
        self.assertEqual(lista,['tomas@aurom.com 85', 'juan@hotmail.com 75', 'maria84@gmail.com 90', 'paquito123@outlook.com 74', 'anaa22@gmail.com 88', 'marcosss@hotmail.com 92'])

    def test_Sort_CorreosCalif(self):
        lista = S(['tomas@hotmail.com 85', 'juan@hotmail.com 75', 'maria84@gmail.com 90', 'paquito123@outlook.com 74', 'anaa22@gmail.com 88', 'marcosss@hotmail.com 92']
    )
        self.assertEqual(lista,[['gmail.com', '88'], ['gmail.com', '90'], ['hotmail.com', '75'], ['hotmail.com', '85'], ['hotmail.com', '92'], ['outlook.com', '74']] )

    def test_promedio(self):
        diccionario = P([['gmail.com', '88'], ['gmail.com', '90'], ['hotmail.com', '75'], ['hotmail.com', '85'], ['hotmail.com', '92'], ['outlook.com', '74']] 
    )
        self.assertEqual(diccionario,{'gmail.com': 89.0, 'outlook.com': 74, 'hotmail.com': 84.0})

if __name__ == '__main__':
    unittest.main()