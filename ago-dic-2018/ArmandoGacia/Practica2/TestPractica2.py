import unittest
import Practica2

class Test_Practica2(unittest.TestCase):
    def TestPractica2(self):
        res=Practica2.calcu([10,3,-2,7,3])
        self.assertEqual(res[0],3)
        self.assertEqual(res[1],2)
        self.assertEqual(res[2],1)
        self.assertEqual(res[3],4)

if __name__ =='__main__':
    unittest.main()
