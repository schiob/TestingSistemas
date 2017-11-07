import unittest
from grading_students import solve

class TestGradingStudents(unittest.TestCase):
    def testGrades(self):
        self.assertEqual(solve([73, 67, 38, 33]),[75, 67, 40, 33] )



if __name__ == '__main__':
    unittest.main()
