import unittest
import p12to24

class Testhora(unittest.TestCase):

    def test_horas(self):
        resultado = p12to24.transforma("2:23p.m.")
        self.assertEqual(resultado, "14:23hrs")
        resultado = p12to24.transforma("11:42p.m.")
        self.assertEqual(resultado, "23:42hrs")
        resultado = p12to24.transforma("11:42a.m.")
        self.assertEqual(resultado, "11:42hrs")
        resultado = p12to24.transforma("12:00a.m.")
        self.assertEqual(resultado, "00:00hrs")
        resultado = p12to24.transforma("12:00p.m.")
        self.assertEqual(resultado, "12:00hrs")
        resultado = p12to24.transforma("1:05a.m.")
        self.assertEqual(resultado, "1:05hrs")
        resultado = p12to24.transforma("11:59p.m.")
        self.assertEqual(resultado, "23:59hrs")

if __name__ == '__main__':
    unittest.main()
