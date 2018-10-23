import unittest
import impares

class imparestest (unittest.TestCase):
    def test_impares(self):
        res=impares.imp([6, -5])
        self.assertEqual(res, 5)

        res=impares.imp([12, 15])
        self.assertEqual(res, 13)

        res=impares.imp([12, 12])
        self.assertEqual(res, 0)

        res=impares.imp([123, 321])
        self.assertEqual(res, 21756)

        res=impares.imp([4321, 1234])
        self.assertEqual(res, 4284911)

        res=impares.imp([-19289, 7853])
        self.assertEqual(res, -77593260)

if __name__ =='__main__':
    unittest.main()
