import io
import unittest
import unittest.mock as mock
from unittest.mock import patch
import archivos


class Tests(unittest.TestCase):
    def testCalc_Prom(self):
        archivoFalso = io.StringIO('10\n10\n6')
        with mock.patch('archivos.open', return_value=archivoFalso, create=True):
            result = int(archivos.calc_prom('miArchivo.txt'))
        self.assertEqual(result, 26)


if __name__ == "__main__":
    unittest.main()
