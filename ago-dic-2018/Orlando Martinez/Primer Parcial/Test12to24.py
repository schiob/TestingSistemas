import unittest
import 12to24.py

class TestHora(unittest.TestCase):
      def test_contar1(self):
          res=12to24.hora(2:23 p.m)
          self.assertEqual(res,14:33 hrs)
      def test_contar1(self):
          res=12to24.hora(11:42 p.m)
          self.assertEqual(res,23:43 hrs)
      def test_contar1(self):
          res=12to24.hora(11:42 a.m)
          self.assertEqual(res,11:42 hrs)
      def test_contar1(self):
          res=12to24.hora(12:00 p.m)
          self.assertEqual(res,12:00 hrs)
      def test_contar1(self):
          res=12to24.hora(12:00 a.m)
          self.assertEqual(res,00:00 hrs)
      def test_contar1(self):
          res=12to24.hora(01:05 a.m)
          self.assertEqual(res,01:05 hrs)
      def test_contar1(self):
          res=12to24.hora(11:59 p.m)
          self.assertEqual(res,23:59 hrs)
if __name__ == '__main__':
    unittest.main()
