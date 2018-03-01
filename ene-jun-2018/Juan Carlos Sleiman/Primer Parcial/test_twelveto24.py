import unittest
from twelveto24 import horario

class TestHorario(unittest.TestCase):

    def test_prueba(self):

        result = horario('02:23p.m.')
        self.assertEqual(r, "14:23hrs")

    def test_prueba1(self):

        result = horario('11:42p.m.')
        self.assertEqual(result, "23:43hrs")

    def test_prueba2(self):

        result = horario('11:42a.m.')
        self.assertEqual(result, "11:42hrs")

    def test_prueba3(self):

        result = horario('12:00p.m.')
        self.assertEqual(r, "00:00hrs")

    def test_prueba4(self):

        result = horario('12:00a.m.')
        self.assertEqual(r, "12:00hrs")

    def test_prueba5(self):

        result = horario('01:05a.m.')
        self.assertEqual(r, "01:05hrs")

    def test_prueba6(self):

        result = horario('11:59p.m.')
        self.assertEqual(r, "23:59hrs")

if __name__ == '__main__':
    unittest.main()
