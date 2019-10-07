import unittest
from TimeConversion import timeConversion

class TestTimeConversion(unittest.TestCase):

    def testHora(self):
        # Primer camino
        self.assertEqual(timeConversion("12:34:34AM"), "00:34:34")

        # Segundo camino
        self.assertEqual(timeConversion("07:45:12AM"), "07:45:12")

        # Tercer camino
        self.assertEqual(timeConversion("12:34:34PM"), "12:34:34")

        # Cuarto camino
        self.assertEqual(timeConversion("07:45:12PM"), "19:45:12")



if __name__ == '__main__':
    unittest.main()
