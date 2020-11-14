import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from calificacionesalumnos import separacionypromediacion

class Testcalificacionesalumnos(unittest.TestCase):
    @patch("pandas.read_csv")
    def test_promedios(self, mock_csv):
        test_cases = (
            {
                "valores": [['Jose_Lopez', 'quimica', 89.0], ['Jose_Lopez', 'matematicas', 85.34], ['Maria_Martinez', 'fisica', 95.5], ['Maria_Martinez', 'español', 90.0]],
                "archivoparcheado": "ejemplo_examen.csv",
                "salida_esperada": [['Jose_Lopez', 87.17], ['Maria_Martinez', 92.75]],
            },
            {
                "valores": [],
                "archivoparcheado": "ejemplo_examen2.csv",
                "salida_esperada": "El archivo no contiene ni una linea de datos",
            },
            {
                "valores": [['Jose_Lopez', 'quimica', 89.0], ['Juan_Daniel', 'matematicas', 85.34], ['Maria_Martinez', 'español', 90.0]],
                "archivoparcheado": "ejemplo_examen3.csv",
                "salida_esperada": [['Jose_Lopez', 89.0], ['Juan_Daniel', 85.34], ['Maria_Martinez', 90.0]],
            },
            {
                "valores": [['Jose_Lopez', 'quimica', 89.0]],
                "archivoparcheado": "ejemplo_examen4.csv",
                "salida_esperada": [['Jose_Lopez', 89.0]],
            },
            {
                "valores": [['Juan_Daniel', 'quimica', 89.0], ['Juan_Daniel', 'matematicas', 85.34], ['Juan_Daniel', 'fisica', 95.5], ['Juan_Daniel', 'español', 90.0]],
                "archivoparcheado": "ejemplo_examen5.csv",
                "salida_esperada": [['Juan_Daniel', 89.96]],
            },
            {
                "valores": [['Luis_Antonio', 'quimica', 89.0], ['Luis_Antonio', 'matematicas', 85.34], ['Luis_Antonio', 'fisica', 95.5], ['Perla_Marisol', 'español', 90.89], ['Perla_Marisol', 'español', 75.42], ['Juan_Daniel', 'español', 70.005]],
                "archivoparcheado": "ejemplo_examen5.csv",
                "salida_esperada": [['Luis_Antonio', 89.95], ['Perla_Marisol', 83.16], ['Juan_Daniel', 70.0]],
            },
        )

        for cp in test_cases:
            def func():
                return cp["valores"]
            mock_csv.return_value = MagicMock()
            mock_csv.return_value.values = MagicMock()
            mock_csv.return_value.values.tolist = func

            salida_real = separacionypromediacion(cp["archivoparcheado"])
            self.assertEqual(salida_real, cp["salida_esperada"])

if __name__ == "__main__":
    unittest.main()