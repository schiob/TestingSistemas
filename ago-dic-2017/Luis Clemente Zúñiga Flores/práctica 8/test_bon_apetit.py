import unittest
from bon_appetit import bonAppetit


class Test_bon_appetit(unittest.TestCase):
    
    
    def setUp(self):
        self.n = 4
        self.k = 1
        self.arr = [3,10,2,9]
        self.b = 12
        
        self.n1 = 4
        self.k1 = 1
        self.arr1 = [3,10,2,9]
        self.b1 = 7
        
        self.n2 = 5 
        self.k2 = 3
        self.arr2 = [4,19,34,2]
        self.b2 = 10
        
        
        
        
    def test_appetit(self):
        self.assertEqual(bonAppetit(self.n,self.k,self.b,self.arr),5)
        
        self.assertEqual(bonAppetit(self.n1,self.k1,self.b1,self.arr1),'Bon Appetit')
        
        self.assertEqual(bonAppetit(self.n2,self.k2,self.b2,self.arr2),-18)
        
        
        
                
        

if __name__ == '__main__':
    unittest.main()
    
    
    
