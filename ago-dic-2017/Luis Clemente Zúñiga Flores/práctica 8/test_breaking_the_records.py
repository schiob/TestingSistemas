import unittest
from breaking_the_records  import getRecord


class Test_breaking_the_record(unittest.TestCase):
    
    
    def setUp(self):
        self.n = 9
        self.lista = [10, 5, 20, 20, 4, 5, 2, 25, 1]
        self.n1 = 10
        self.lista1 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
        self.n2 = 20
        self.lista2 = [2, 3, 56, 71, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 13, 45, 23, 56, 23, 1]
        
    def test_breaking(self):
        self.assertEqual(getRecord(self.lista),(2,4))
        self.assertEqual(getRecord(self.lista1),(4,0))
        self.assertEqual(getRecord(self.lista2),(3,1))

if __name__ == '__main__':
    unittest.main()
    
    
    
