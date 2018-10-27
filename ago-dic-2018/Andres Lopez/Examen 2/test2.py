import unittest
import tarea

class foquito(unittest.TestCase):

   def test1(self):
        res = tarea.foquito(0000)
        self.assertEqual(res, 24)
        
   def test2(self):
        res = tarea.foquito(10)
        self.assertEqual(res, 8)
        
   def test3(self):
        res = tarea.foquito(675)
        self.assertEqual(res, 14)
        
   def test4(self):
        res = tarea.foquito(2018)
        self.assertEqual(res, 20)
        
   def test5(self):
        res = tarea.foquito(666)
        self.assertEqual(res, 18)
        
   def test6(self):
        res = tarea.foquito(18361)
        self.assertEqual(res, 22)
        
   def test7(self):
        res = tarea.foquito(9625)
        self.assertEqual(res,25)
        
if __name__ == '__main__':
    unittest.main()
