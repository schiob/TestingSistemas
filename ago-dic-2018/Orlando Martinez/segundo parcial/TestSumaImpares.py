import unittest
import SumaImpares

class TestSumaImpares(unittest.TestCase):
      def test_1(self):
          res=SumaImpares.Sumar(6,-5)
          self.assertEqual(res,5)
      def test_2(self):
          res=SumaImpares.Sumar(12,15)
          self.assertEqual(res,13)
      def test_3(self):
          res=SumaImpares.Sumar(12,12)
          self.assertEqual(res,0)
      def test_4(self):
          res=SumaImpares.Sumar(123,321)
          self.assertEqual(res,21756)
      def test_5(self):
          res=SumaImpares.Sumar(4321,1234)
          self.assertEqual(res,4284911)
      def test_6(self):
         res=SumaImpares.Sumar(-19289,7853)
         self.assertEqual(res,-77593260)



if __name__ == '__main__':
    unittest.main()
