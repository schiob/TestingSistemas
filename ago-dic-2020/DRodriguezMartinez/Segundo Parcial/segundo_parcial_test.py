from  unittest import mock, TestCase
from segundo_parcial import calcular_promedio

class segundo_parcial_test(TestCase):

    def testChio(self):
        esperado = {'Jose_Lopez': 87.17, 'Maria_Martinez': 92.75}
        used_mock = "Jose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34\nMaria_Martinez fisica 95.50\nMaria_Martinez español 90.00"

        with mock.patch('segundo_parcial.open') as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = used_mock
            real = calcular_promedio("Mock")

            assert esperado == real 

    def testResultadosNormales(self):
        esperado = {'Daniela_Rodriguez': 95, 'Maria_Martinez': 92.75, 'Persona_1': 85.2} 
        used_mock = "Daniela_Rodriguez quimica 95\nDaniela_Rodriguez matematicas 95\nMaria_Martinez fisica 95.50\nMaria_Martinez español 90.00\nPersona_1 quimica 85.2"

        with mock.patch('segundo_parcial.open') as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = used_mock
            real = calcular_promedio("Mock")

            assert esperado == real 

    def testSinDatos(self):
        esperado = {}
        used_mock = ""

        with mock.patch('segundo_parcial.open') as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = used_mock
            real = calcular_promedio("Mock")

            assert esperado == real

    def testCalificacionSinNumeros(self):
        used_mock = "Jose_Lopez quimica 89.00\nJose_Lopez matematicas 85.34\nMaria_Martinez fisica 95.50\nMaria_Martinez español A"

        with mock.patch('segundo_parcial.open') as mock_open:

            mock_open.return_value.__enter__.return_value.read.return_value = used_mock
            with self.assertRaisesWithMessage(ValueError):
                calcular_promedio("mock")

    def testNumerosNegativos(self):
        used_mock = "Jose_Lopez quimica -89.00\nJose_Lopez matematicas -85.34\nMaria_Martinez fisica -95.50\nMaria_Martinez español -90.00"

        with mock.patch('segundo_parcial.open') as mock_open:

            mock_open.return_value.__enter__.return_value.read.return_value = used_mock
            with self.assertRaisesWithMessage(ValueError):
                calcular_promedio("mock")

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")