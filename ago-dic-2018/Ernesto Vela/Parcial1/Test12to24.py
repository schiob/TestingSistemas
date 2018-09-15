import unittest
import 12to24

class horaTest(unittest.TestCase):

    def test_12to14(self):
        res = 12to24.hora("02:23")
        self.assertEqual(res, "14:23:00")

        res = 12to24.hora("11:42")
        self.assertEqual(res, "23:43:00")

        res = 12to24.hora("11:42")
        self.assertEqual(res, "11:42:00")

        res = 12to24.hora("12:00")
        self.assertEqual(res, "00:00:00")

        res = 12to24.hora("12:00")
        self.assertEqual(res, "12:00:00")

        res = 12to24.hora("01:05")
        self.assertEqual(res, "01:05:00")

        res = 12to24.hora("11,59")
        self.assertEqual(res, "23:59:00")


if __name__== '__main__':
    unittest.main()
