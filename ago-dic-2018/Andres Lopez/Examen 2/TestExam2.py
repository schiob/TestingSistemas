import unittest
import Exam2

class Test (unittest.TestCase):
    
    def test_TestExam2(self):
        res=Exam2.Exam2([6,-5])
        self.assertEqual(res,5)
        
    def test_TestExam2(self):
        res=Exam2.Exam2([12,15])
        self.assertEqual(res,13)
        
    def test_TestExam2(self):
        res=Exam2.Exam2([12,12])
        self.assertEqual(res,0)

    def test_TestExam2(self):
        res=Exam2.Exam2([123,321])
        self.assertEqual(res,21756)

    def test_TestExam2(self):
        res=Exam2.Exam2([4321,1234])
        self.assertEqual(res,4284911)

    def test_TestExam2(self):
        res=Exam2.Exam2([-19289,7853])
        self.assertEqual(res,-77593260)
        
if __name__ =='__main__':
    unittest.main()
