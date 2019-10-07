import unittest
import Sumaimpares

class Test (unittest.TestCase):
    def test_sumaimpares(self):
        res=Sumaimpares.sumatoria([6,-5])
        self.assertEqual(res, 5)
    def test_sumaimpares2(self):
        res=Sumaimpares.sumatoria([12,15])
        self.assertEqual(res, 13)
    def test_sumaimpares3(self):
        res=Sumaimpares.sumatoria([12,12])
        self.assertEqual(res, 0)
    def test_sumaimpares4(self):
        res=Sumaimpares.sumatoria([123,321])
        self.assertEqual(res, 21756)
    def test_sumaimpares5(self):
        res=Sumaimpares.sumatoria([4321,1234])
        self.assertEqual(res, 4284911)
    def test_sumaimpares6(self):
        res=Sumaimpares.sumatoria([-19289,7853])
        self.assertEqual(res, -77593260)

if __name__ == '__main__':
    unittest.main()
