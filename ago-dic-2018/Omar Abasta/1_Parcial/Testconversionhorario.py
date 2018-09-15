import unittest
from ConversionDeHora import ConversionHora

class TestConversionHora(unittest.TestCase):

    def setUp(self):
        pass

    def testConversionHora1(self):
        result=ConversionHora("02:23:00PM"),
        self.assertEqual(ConversionHora(result,"14:23:00")

    def testConversionHora2(self):
        result=ConversionHora("11:42:00PM"),
        self.assertEqual(ConversionHora(result,"23:42:00")

    def testConversionHora3(self):
        result=ConversionHora("11:42:00AM"),
        self.assertEqual(ConversionHora(result,"11:42:00")

    def testConversionHora4(self):
        result=ConversionHora("12:00:00AM"),
        self.assertEqual(ConversionHora(result,"00:00:00")

    def testConversionHora5(self):
        result=ConversionHora("12:00:00PM"),
        self.assertEqual(ConversionHora(result,"00:00:00")

    def testConversionHora6(self):
        result=ConversionHora("01:05:00AM"),
        self.assertEqual(ConversionHora(result,"01:05:00")

    def testConversionHora7(self):
        result=ConversionHora("11:59:00AM"),
        self.assertEqual(ConversionHora(result,"23:59:00")




if __name__ == '__main__':
    unittest.main()
