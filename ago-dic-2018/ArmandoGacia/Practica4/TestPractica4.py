import unittest
import Practica4

class Test_leds(unittest.TestCase):
    #Test 1 <1,2>
    def Test1_(self):
        res=Practica4.leds('1')
        self.assertEqual(res,2)
    #Test 2 <32,10>
    def Test2(self):
        res=Practica4.leds('32')
        self.assertEqual(res,10)
    #Test 3 <8888,28>
    def Test3(self):
        res=Practica4.leds('8888')
        self.assertEqual(res,28)
    #Test 4 <115380,27>
    def Test4(self):
        res=Practica4.leds('115380')
        self.assertEqual(res,27)
    #Test 5 <2819311,29>
    def Test5(self):
        res=Practica4.leds('2819311')
        self.assertEqual(res,29)
    #Test 6 <23456,25>
    def Test6(self):
        res=Practica4.leds('23456')
        self.assertEqual(res,25)

if __name__ =='__main__':
    unittest.main()
