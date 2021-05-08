from unittest import mock, TestCase
import segundo_parcial

class segundo_parcial_tests(TestCase):

    def test_Inicial(self):
        esperado="textoEsperado"
        used_mock="textoEsperado"

        with mock.patch('prueba.txt') as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value=used_mock
            real=segundo_parcial.checkArchivoExiste("Mock")

            assert esperado==real

    def test_funciones(self):
        esperado="{ \"INPUT\": \"SegundotextoEsperado\" , \"OUTPUT\": \"SEGUNDOTEXTOESPERADO\"}"
        used_mock="textoEsperado"

        with mock.patch('prueba.txt') as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value=used_mock
            real=segundo_parcial.funcionFinal("Mock")

            assert esperado==real