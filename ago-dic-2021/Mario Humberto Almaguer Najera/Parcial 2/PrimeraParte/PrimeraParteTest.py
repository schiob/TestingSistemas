import unittest
from unittest import mock
from unittest.mock import mock_open, patch
from PrimeraParte import PrimeraParte

class PrimeraParteTest(unittest.TestCase):

    def test_archivo_mock(self):
        # Datos para posteriormente eliminar la dependencia del archivo
        datos = """nombreMock1 materiaMock 68.00
nombreMock1 materiaMock 98.00
nombreMock2 materiaMock 82.00
nombreMock2 materiaMock 90.00"""

        # Hacer el mock
        mock_archivo = mock_open(read_data=datos)

        # Salida esperada en base a los datos
        salda_esperada = ['nombreMock1 83.0', 'nombreMock2 86.0']

        with patch('builtins.open', mock_archivo):
            pp = PrimeraParte()

            # Llamar al metodo que calcula los promedios y lee el archivo
            # Esto ya me deberia de regresar los datos como mock, incluso el archivo datos.txt podria estar vacio
            # y funcionar
            resultado = pp.leer_archivo()

        self.assertEqual(resultado, salda_esperada)

    def test_sin_calificaciones(self):
        # Datos para posteriormente eliminar la dependencia del archivo
        datos = """nombreMock1 materiaMock
nombreMock1 materiaMock
nombreMock2 materiaMock
nombreMock2 materiaMock"""

        # Hacer el mock
        mock_archivo = mock_open(read_data=datos)

        # Salida esperada en base a los datos
        salda_esperada = 'No hay columna calificacion en el archivo'

        with patch('builtins.open', mock_archivo):
            pp = PrimeraParte()

            # Llamar al metodo que calcula los promedios y lee el archivo
            # Esto ya me deberia de regresar los datos como mock, incluso el archivo datos.txt podria estar vacio
            # y funcionar
            resultado = pp.leer_archivo()

        self.assertEqual(resultado, salda_esperada)

    def test_sin_nombres(self):
        # Datos para posteriormente eliminar la dependencia del archivo
        datos = """ materiaMock 68.00
 materiaMock 98.00
 materiaMock 82.00
 materiaMock 90.00"""

        # Hacer el mock
        mock_archivo = mock_open(read_data=datos)

        # Salida esperada en base a los datos
        salda_esperada = 'No hay columna nombre en el archivo'

        with patch('builtins.open', mock_archivo):
            pp = PrimeraParte()

            # Llamar al metodo que calcula los promedios y lee el archivo
            # Esto ya me deberia de regresar los datos como mock, incluso el archivo datos.txt podria estar vacio
            # y funcionar
            resultado = pp.leer_archivo()

        self.assertEqual(resultado, salda_esperada)



if __name__ == '__main__':
    unittest.main()