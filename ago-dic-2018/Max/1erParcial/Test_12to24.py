import unittest
import 12to24 import reloj

class Test_hora(unittest.TestCase):
    def test_prueba(self):
        res = horario('02:23p.m')
        self.assertEqual(res, "14:23hrs")

    def test_prueba1(self):
        res = horario('11:42p.m')
        self.assertEqual(res, "23:43hrs")

    def test_prueba2(self):
        res = horario('11:42a.m')
        self.assertEqual(res, "11:42hrs")

    def test_prueba3(self):
        res = horario('12:00p.m')
        self.assertEqual(res, "00:00hrs")

    def test_prueba4(self):
        res = horario('12:00a.m')
        self.assertEqual(res, "12:00hrs")

    def test_prueba5(self):
        res = horario('01:05a.m')
        self.assertEqual(res, "01:05hrs")

    def test_prueba6(self):
        res = horario('11:59p.m')
        self.assertEqual(res, "23:59hrs")

if __name__ == '__main__':
    unittest.main()
