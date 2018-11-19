import unittest
import Practica2

class p2test (unittest.TestCase):
    def test_Practica2(self):
        res=Practica2.calc(5, [1, 2, 10, 40, 63])
        self.assertEqual(res[0], 3)
        self.assertEqual(res[1], 2)
        self.assertEqual(res[2], 5)
        self.assertEqual(res[3], 0)

        res=Practica2.calc(3, [-20, 999, 0])
        self.assertEqual(res[0], 2)
        self.assertEqual(res[1], 1)
        self.assertEqual(res[2], 2)
        self.assertEqual(res[3], 1)

        res=Practica2.calc(7, [-111, 1, 0, 57, 80, 74, 4])
        self.assertEqual(res[0], 4)
        self.assertEqual(res[1], 3)
        self.assertEqual(res[2], 6)
        self.assertEqual(res[3], 1)

if __name__ =='__main__':
    unittest.main()
