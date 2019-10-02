import unittest
from datetime import datetime


def convert24to12(hora):
    hora = datetime.strptime(hora,'%H:%M')
    return hora.strftime("%I:%M %p")


class test24to12(unittest.TestCase):


    def test_1423(self):
        prueba = convert24to12("14:23")
        self.assertEqual(prueba, "02:23 PM")

    def test_2343(self):
        prueba = convert24to12("23:43")
        self.assertEqual(prueba, "11:43 PM")

    def test_1142(self):
        prueba = convert24to12("11:42")
        self.assertEqual(prueba, "11:42 AM")

    def test_0000(self):
        prueba = convert24to12("00:00")
        self.assertEqual(prueba, "12:00 AM")

    def test_1200(self):
        prueba = convert24to12("12:00")
        self.assertEqual(prueba, "12:00 PM")

    def test_1005(self):
        prueba = convert24to12("01:05")
        self.assertEqual(prueba, "01:05 AM")

    def test_2359(self):
        prueba = convert24to12("23:59")
        self.assertEqual(prueba, "11:59 PM")


if __name__ == '__main__':
     unittest.main()
