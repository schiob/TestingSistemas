import unittest
import examen
class Test_examen(unittest.TestCase):
    def Test1(self):
#caso de prueba 1
        n=examen.hora("02:23p.m.")
        self.assertEqual(n,"14:23hrs")
    def Test2(self):
#caso de prueba 1
        n=examen.hora("11:42p.m.")
        self.assertEqual(n,"23:23hrs")
    def Test1(self):
#caso de prueba 1
        n=examen.hora("11:42a.m.")
        self.assertEqual(n,"14:23hrs")
