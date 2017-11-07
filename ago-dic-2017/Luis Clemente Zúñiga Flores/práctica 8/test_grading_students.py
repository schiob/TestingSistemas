import unittest
from grading_students  import solve


class Test_breaking_the_record(unittest.TestCase):
    
    
    def setUp(self):
        n = 4
        self.grades = [73,67,38,33]
        self.salida= [75,67,40,33]
        
        n1 = 5
        self.grades1 = [67,34,100,20]
        self.salida1 = [67, 34, 100, 20]

        n2 = 20
        self.grades2 = [88,25,90,100,90,40,35,12,19,90,12,56,77,67,49,35,70,70,99,87,69]
        self.salida2 = [90, 25, 90,100,90,40,35,12,19,90,12,56,77,67,50,35,70,70,100,87,70]


        
    def test_breaking(self):
        self.assertEqual(solve(self.grades),self.salida)
        
        self.assertEqual(solve(self.grades1),self.salida1)
        self.assertEqual(solve(self.grades2),self.salida2)


if __name__ == '__main__':
    unittest.main()
