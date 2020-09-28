import unittest
from Practica4 import extract_data, calcular_promedio_deCSV

class TestPractica4CSV(unittest.TestCase):

    test_cases = (
            {
                "filename": "practica4File.csv",
                "esperado": {'hotmail.com': 84.0, 'gmail.com': 89.0, 'outlook.com': 74.0},
                "hasError": False

            },
            {
                "filename": "practica4File2.csv",
                "esperado": {'proton.com': 95.0, 'gmail.com': 89.0},
                "hasError": False
            },
            {
                "filename": "practica4File3.csv",
                "esperado": {},
                "hasError": False
            },
            {
                "filename": "practica4File4.csv",
                "esperado": "",
                "hasError": True
            }
            )

    def testCSV(self):
        for tc in self.test_cases:
            print(tc["filename"])
            if tc["hasError"]:
                with self.assertRaises(ValueError):
                    extract_data(tc["filename"])
            else:
                salida_real = calcular_promedio_deCSV(tc["filename"])
                self.assertEqual(salida_real, tc["esperado"])

if __name__ == '__main__':
    unittest.main()