import re
import unittest
from unittest.mock import Mock, patch

def leerArchivo(path):
    txt = path
    txt = re.sub('[^a-zA-Z0-9]', ' ', txt)
    return txt

strings = ['', 'en este archivo se le borran algunas partes !@##$%%^&&*()_+ <><><>#%$%^&*%^@@', 'a este string no se le cambia nada']
results = ['', 'en este archivo se le borran algunas partes                                  ', 'a este string no se le cambia nada']

class Test_Leer_Archivo(unittest.TestCase):
    
    def test_archivo_nulo(self):
        direccion2 = strings[0]
        self.assertEqual(leerArchivo(direccion2), '')
                         
    def test_archivo_remover(self):
        direccion3 = strings[1]
        self.assertEqual(leerArchivo(direccion3), 'en este archivo se le borran algunas partes                                  ')
    
    def test_archivo_sin_correcion(self):
        direccion4 = strings[2]
        self.assertEqual(leerArchivo(direccion4), 'a este string no se le cambia nada')
        
class Test_leerArchivo(unittest.TestCase):
    @patch('builtins.open')
    def test_leer(self, mock_open):
        for r in range(len(strings)):
            mock_open.return_value.read.return_value = results[r]
            res = leerArchivo(strings[r])
            resultado = results[r]
            print('string: ', res)
            print('resultado:', resultado)
            self.assertEqual(res, resultado)
        #mock_Archivo = Mock()
        #unit_leer.leerArchivo(mock_Archivo)
        #print(mock_Archivo.mock_calls)
        
if __name__ == '__main__':
    unittest.main()