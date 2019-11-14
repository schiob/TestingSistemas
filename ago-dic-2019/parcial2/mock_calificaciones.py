import unittest
import calificaciones as cal
from unittest.mock import Mock
from unittest.mock import patch
import mock

class TestCalificaciones(unittest.TestCase):
    def testExtrapolate(self):
        en = ["12 10 12", "98 12 90", "abc djfgh xyz", "True False True", "a b c"]
        sa = [["12", "12"], ["98", "90"], ["abc", "xyz"], ["True", "True"], ['a', 'c']]

        for r in range(len(en)):
            with self.subTest(r=r):
                entrada = en[r]
                salidad_esperada = sa[r]
                salida_actual = cal.extrapolate(entrada)
                self.assertEqual(salida_actual, salidad_esperada)

    def testDividirPorAlumno(self):
        en = [ ['Jose_Lopez quimica 89.00\n', 'Jose_Lopez matematicas 85.34\n', 'Maria_Martinez fisica 95.50\n', 'Maria_Martinez espaÃ±ol 90.00\n', 'Carlos_Trejo sdjs 100.00\n', 'Carlos_Trejo sdd 80.00\n', 'Carlos_Trejo dfgf 50.00\n', 'Carlos_Trejo trghfg 30.00\n', 'Carlos_Trejo reigjfr 70.00\n', 'Carlos_Trejo ss 10.00\n'],
                ]
        sa = [{'Jose_Lopez': ['89.00', '85.34'], 'Maria_Martinez': ['95.50', '90.00'], 'Carlos_Trejo': ['100.00', '80.00', '50.00', '30.00', '70.00', '10.00']}
                ]
        for r in range(len(en)):
            with self.subTest(r=r):
                entrada = en[r]
                salidad_esperada = sa[r]
                salida_actual = cal.dividirporalumno(entrada)
                self.assertEqual(salida_actual, salidad_esperada)

    @mock.patch('calificaciones.archtolst')
    def testMain(self, mock_open):
        en = [["Jose_Lopez quimica 89.00",
        "Jose_Lopez matematicas 85.34",
        "Maria_Martinez fisica 95.50",
        "Maria_Martinez español 90.00"],

        ["Carlos_Trejo sdjs 100.00",
        "Carlos_Trejo sdd 80.00",
        "Carlos_Trejo dfgf 50.00",
        "Carlos_Trejo trghfg 30.00",
        "Carlos_Trejo reigjfr 70.00",
        "Carlos_Trejo ss 10.00"]]

        sa = ["Jose_Lopez 87.17\nMaria_Martinez 92.75\n",
        "Carlos_Trejo 56.67\n"]

        for r in range(len(en)):
            with self.subTest(r=r):
                entrada = en[r]
                salidad_esperada = sa[r]

                mock_open.return_value = entrada
                salida_actual = cal.main("smtg")

                self.assertEqual(salida_actual, salidad_esperada)


if __name__ == '__main__':
    unittest.main()
