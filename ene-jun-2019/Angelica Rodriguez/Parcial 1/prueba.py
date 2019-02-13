import unittest
import hoursToHours
class TestLados(unittest.TestCase):

    def test_hours(self):
        """función para correr casos de prueba"""
        test_cases = [("14:23hrs","02:23p.m."),
                      ("04:42hrs","04:42a.m.")]

        for inp in test_cases:   # corremos cada caso de prueba
            expected = inp[1] 
            actual = hoursToHours.convertHours(inp[0])
            self.assertEqual(expected, actual)  # comparación

if __name__ == '__main__':
    unittest.main()
