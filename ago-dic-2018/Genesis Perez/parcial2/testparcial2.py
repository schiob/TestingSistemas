import unittest
import parcial2

class Testparcial2(unittest.TestCase):
      def prueba1(self):
          res=parcial2.sumaimpares(6,-5)
          self.assertEqual(res,5)
      def prueba2(self):
          res=parcial2.sumaimpares(12,15)
          self.assertEqual(res,13)
      def prueba3(self):
          res=parcial2.sumaimpares(12,12)
          self.assertEqual(res,0)
      def prueba4(self):
          res=parcial2.sumaimpares(123,321)
          self.assertEqual(res,21756)
      def prueba5(self):
          res=parcial2.sumaimpares(4321,1234)
          self.assertEqual(res,4284911)
      def prueba6(self):
         res=parcial2.sumaimpares(-19289,7853)
         self.assertEqual(res,-77593260)

if __name__ == '__main__':
    unittest.main()
