import unittest
import hoursToHours
class TestPruebas(unittest.TestCase):

    def test_hours(self):
        """función para correr casos de prueba"""
        test_cases = [("14:23hrs","02:23p.m."),
                      ("23:43hrs","11:43p.m."),
                      ("11:42hrs","11:42a.m."),
                      ("00:00hrs","12:00a.m."),
                      ("12:00hrs","12:00p.m."),
                      ("01:05hrs","01:05a.m."),
                      ("23:59p.m.","11:59p.m.")]

        for inp in test_cases:   # corremos cada caso de prueba
            expected = inp[1]
            actual = hoursToHours.convertHours(inp[0])
            self.assertEqual(expected, actual)  # comparación

if __name__ == '__main__':
    unittest.main()
