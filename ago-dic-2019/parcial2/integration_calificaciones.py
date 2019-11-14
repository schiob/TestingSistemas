import unittest
import calificaciones as cal
import os
## -*- coding: utf-8 -*-

class TestCalificaciones(unittest.TestCase):
    archivo = ["""Jose_Lopez quimica 89.00
    Jose_Lopez matematicas 85.34
    Maria_Martinez fisica 95.50
    Maria_Martinez español 90.00""",
    """Carlos_Trejo sdjs 100.00
    Carlos_Trejo sdd 80.00
    Carlos_Trejo dfgf 50.00
    Carlos_Trejo trghfg 30.00
    Carlos_Trejo reigjfr 70.00
    Carlos_Trejo ss 10.00"""
    ]

    path = "test.txt"

    resultado_esp = ["Jose_Lopez 87.17\nMaria_Martinez 92.75\n", "Carlos_Trejo 56.67\n"]

    def setu(self, r):
        f = open(self.path, "w+")
        f.write(self.archivo[r])
        f.close()

    def down(self, p):
        os.remove(p)

    def testMain(self):
        for r in range(len(self.archivo)):
            self.setu(r)
            with self.subTest(r=r):
                salidad_esperada = self.resultado_esp[r]
                salida_actual = cal.main(self.path)
                self.assertEqual(salida_actual, salidad_esperada)
            self.down(self.path)

if __name__ == '__main__':
    unittest.main()
