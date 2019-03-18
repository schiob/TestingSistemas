import unittest
import hora

class TestHora(unittest.TestCase):
    def test_hora(self):
        test_casos=(
        ("14:23", "02:23p.m."),
        ("23:43", "11:43p.m."),
        ("11:42", "11:42a.m."),
        ("00:00", "12:00a.m."),
        ("12:00", "12:00p.m."),
        ("01:05", "01:05a.m."),
        ("23:59", "11:59p.m.")
        )

        for hora, esperado in test_casos:
            actual = hora.mostrar(hora)
            self.assertEqual(esperado, actual)

if __name__ == '__main__':
    unittest.main()