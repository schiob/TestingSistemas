import unittest
from Calificaciones import calificar

class TestCal(unittest.TestCase):
    def cal_test(self):
        test= [
             {   "input": "alumnos.txt",
                 "expect_out": "('Jose_Lopez', 87.33)"
             }
        ]
        for tc in test :
            actual = calificar(tc["input"])
            self.assertEquals(tc["expect_out"],actual)
    

if __name__ == "__main__":
    unittest.main()
