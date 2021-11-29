import io
import unittest
import unittest.mock as mock
from unittest.mock import patch
import parcial2
import escritor


class Tests(unittest.TestCase):
    def test_promedios(self):
        archivoFalso = io.StringIO(
            "juan_perez fisica 70\njuan_perez probabilidad 50\npedro_mendoza fisica 70\npedro_mendoza probabilidad 90")
        with mock.patch('parcial2.open', return_value=archivoFalso, create=True):
            result = parcial2.part1.calificaciones(archivoFalso)
        self.assertEqual(result, [['juan_perez', '70.00'], ['juan_perez', '60.00'], [
                         'pedro_mendoza', '70.00'], ['pedro_mendoza', '70.00']])

    @patch("escritor.usaEscritor.escribir")
    def test_test_escribir(self, mock_suma):
        mock_suma.return_value = 50
        suma = escritor.usaEscritor().escribir()
        self.assertEqual(escritor.usaEscritor().escribir(), suma)


if __name__ == "__main__":
    unittest.main()
