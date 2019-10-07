import unittest
import PrimerParcial

class TestHora(unittest.TestCase):
    def test_hora(self):
        test_casos = (("14:23hrs", "02:23p.m."),
                     ("23:43hrs", "11:43p.m."),
                     ("11:42hrs", "11:42a.m."),
                     ("00:00hrs", "12:00a.m."),
                     ("12:00hrs", "12:00p.m."),
                     ("01:05hrs", "01:05a.m."),
                     ("23:59hrs", "11:59p.m."))

        for hora,esperado in test_casos:
            actual = PrimerParcial.cambio(hora)
            self.assertEqual(esperado,actual)

if __name__ == '__main__':
    unittest.main()