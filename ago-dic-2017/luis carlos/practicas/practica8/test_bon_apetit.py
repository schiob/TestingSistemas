import unittest
from bon_appetit import bonAppetit
class bon_Appetit(unittest.TestCase):
    def setUp(self):
        self.n=5
        self.ar = 6,6,6,6,6
        #k indice que ana no comio
        self.k=3
        self.b=15
                           

    def test_bonAppetite(self):
        self.assertEqual(bonAppetit(self.n,self.k,self.b,self.ar),"Bon Appetit")

    def test_bonAppetiteDifferent(self):
        self.assertEqual(bonAppetit(self.n,self.k,self.b,self.ar),20)

if __name__ == '__main__':
    unittest.main()

                  
