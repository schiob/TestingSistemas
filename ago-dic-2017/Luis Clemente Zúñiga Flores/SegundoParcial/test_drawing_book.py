import unittest
from drawing_book import solve


class Test_drawing_book(unittest.TestCase):
    
    
    def setUp(self):
       self.n_par = 100
       self.n_impar = 101
       self.p = 1
              
    def test_primera_pagina_par(self):
        self.assertEqual(solve(self.n_par,self.p),0)
    
    def test_primera_pagina_impar(self):
        self.assertEqual(solve(self.n_impar,self.p),0)
          
    def test_ultima_pagina_par(self):
        self.assertEqual(solve(self.n_impar,self.n_impar),0)
    
    def test_ultima_pagina_impar(self):
        self.assertEqual(solve(self.n_impar,self.n_impar),0)
          
    def test_pagina_central_par(self):
        self.assertEqual(solve(self.n_par, self.n_par/2),25)
            
    def test_pagina_central_impar(self):
        self.assertEqual(solve(self.n_impar, self.n_par/2),25)    

    def test_pagina_primera_mitad_par(self):
        self.assertEqual(solve(self.n_par,20),10)
        
    def test_pagina_primera_mitad_impar(self):
        self.assertEqual(solve(self.n_impar,20),10)
   
    def test_pagina_segunda_mitad_par(self):
        self.assertEqual(solve(self.n_par,60),20)
        
    def test_pagina_segunda_mitad_impar(self):
        self.assertEqual(solve(self.n_impar,60),20)
                    
    

if __name__ == '__main__':
    unittest.main()
    
    
    
