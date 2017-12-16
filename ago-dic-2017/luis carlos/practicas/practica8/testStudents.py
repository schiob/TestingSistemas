import unittest
from grading_students import solve
class gradingStudents(unittest.TestCase):
    def test_grades(self):
        self.assertEqual(solve([73,67,38,33]),([75,67,40,33]))

    def test_grades_two(self):
        self.assertEqual(solve([79,69,39,30]),([80,70,40,30]))

if __name__=='__main__':
    unittest.main()
