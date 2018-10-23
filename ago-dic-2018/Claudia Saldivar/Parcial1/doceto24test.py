import unittest
from doceto24 import horario


class TestHora(unittest.TestCase):

    def test_1(self):
        hi = horario("02:23 PM") 
        self.assertEqual(hi, "14:23:00")

    def test_2(self):
        hi = horario("11:42")
        self.assertEqual(hi, "23:43:00")

    def test_3(self):
        hi = horario("11:42")
        self.assertEqual(hi, "11:42:00")

    def test_4(self):
        hi = horario("12:00")
        self.assertEqual(hi, "00:00:00")

    def test_5(self):
        hi = horario("12:00")
        self.assertEqual(hi, "12:00:00")

    def test_6(self):
        hi = horario("01:05")
        self.assertEqual(hi, "01:05:00")

    def test_7(self):
        hi = horario("11,59")
        self.assertEqual(hi, "23:59:00")


if __name__== '__main__':
    unittest.main()
