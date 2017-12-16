import unittest
from breakings_the_records import getRecord
class test_breakinRecords(unittest.TestCase):
    

    def test_breaking_records(self):
        self.assertEqual((getRecord([5,5,5,1,10,6,6,3,3,2])),(1,1))

    def test_breaking_records_two(self):
        self.assertEqual((getRecord([1,1,1,1,1,1,5,0,3,4])),(1,1))
        

if __name__=='__main__':
    unittest.main()
    
