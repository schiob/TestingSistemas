import unittest
from main import main
from unittest.mock import patch, MagicMock
from report import genReport
from mensaje import MensajeBonito
from caluculos import CalcPromedio

class TestIntegrationTopDown(unittest.TestCase):

    @patch("builtins.print")
    @patch("builtins.input")
    def test_Integral1(self, mock_input, mock_print):
        # Storage real, Mock de Reporte
        mock_input.return_value = "1"
        mock_genReport = MagicMock()
        mock_genReport.return_value = "Mi reporte"

        self.assertEqual(main(mock_genReport, None, None), "Mi reporte")
    
    @patch("builtins.print")
    @patch("builtins.input")
    def test_Integral2(self, mock_input, mock_print):
        # Storage real, Mock de Reporte
        mock_input.return_value = "1"

        mock_promediador = MagicMock()
        mock_promediador.return_value = 87

        mock_genMensaje = MagicMock()
        mock_genMensaje.return_value = "MENSAJE DEL FINAL"

        salida_esperada = '''REPORTE
El alumno Ana tiene las sig calificaciones:
Mate 90
Español 75
Ingles 70

Con un promedio de 87

GRACIAS
MENSAJE DEL FINAL
'''

        self.assertEqual(main(genReport, mock_promediador, mock_genMensaje), salida_esperada)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_Integral3(self, mock_input, mock_print):
        # Storage real, Mock de Reporte
        mock_input.return_value = "1"

        mock_promediador = MagicMock()
        mock_promediador.return_value = 87

        salida_esperada = '''REPORTE
El alumno Ana tiene las sig calificaciones:
Mate 90
Español 75
Ingles 70

Con un promedio de 87

GRACIAS
Why? Because fuck you, that's why. - escuelita
'''

        self.assertEqual(main(genReport, mock_promediador, MensajeBonito), salida_esperada)
    
    @patch("builtins.print")
    @patch("builtins.input")
    def test_Integral4(self, mock_input, mock_print):
        # Storage real, Mock de Reporte
        mock_input.return_value = "1"

        salida_esperada = '''REPORTE
El alumno Ana tiene las sig calificaciones:
Mate 90
Español 75
Ingles 70

Con un promedio de 78.33333333333333

GRACIAS
Why? Because fuck you, that's why. - escuelita
'''

        self.assertEqual(main(genReport, CalcPromedio, MensajeBonito), salida_esperada)

if __name__ == "__main__":
    unittest.main()