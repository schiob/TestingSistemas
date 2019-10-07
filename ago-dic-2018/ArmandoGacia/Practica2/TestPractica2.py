import unittest
import Practica2

class Test_Practica2(unittest.TestCase):
    def TestPractica2(self):
#caso de prueba 1
        res=Practica2.calcu([10,3,-2,7,3])
        self.assertEqual(res[0],3)
        self.assertEqual(res[1],2)
        self.assertEqual(res[2],1)
        self.assertEqual(res[3],4)

#caso de prueba 2
        res=Practica2.calcu([-5,-3,-2,8,6])
        self.assertEqual(res[0],2)
        self.assertEqual(res[1],3)
        self.assertEqual(res[2],3)
        self.assertEqual(res[3],2)

#caso de prueba 3
        res=Practica2.calcu([12,5,15,7,3])
        self.assertEqual(res[0],4)
        self.assertEqual(res[1],1)
        self.assertEqual(res[2],0)
        self.assertEqual(res[3],5)

#caso de prueba 4
        res=Practica2.calcu([-4,-12,-2,-8,-10])
        self.assertEqual(res[0],0)
        self.assertEqual(res[1],5)
        self.assertEqual(res[2],5)
        self.assertEqual(res[3],0)

if __name__ =='__main__':
    unittest.main()
