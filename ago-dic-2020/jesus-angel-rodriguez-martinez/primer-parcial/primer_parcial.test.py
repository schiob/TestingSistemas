import os
import unittest
from primer_parcial import tri_from_file

class tri_from_file_test(unittest.TestCase):
    def testEquilatero(self):
        test_cases = (
            {"file_path" : "test.txt",  "sides": "4 4 4", "type": "Equilátero"},
            {"file_path" : "equi1.txt", "sides": "3 3 3", "type": "Equilátero"},
            {"file_path" : "equi2.txt", "sides": "5 5 5", "type": "Equilátero"},  
        )
        for tc in test_cases:
            f = open(tc['file_path'], "w")
            f.write(tc['sides'])
            f.close()
            self.assertEqual(tri_from_file(tc['file_path']), tc['type'])
            os.remove(tc['file_path'])
            
    def testNoTri(self):
        test_cases = (
            {"file_path" : "notri1.txt",  "sides": "0 0 0", "type": "No triángulo"},
            {"file_path" : "notri2.txt", "sides": "0 5 7", "type": "No triángulo"},
            {"file_path" : "notri3.txt", "sides": "1 2 3", "type": "No triángulo"},  
        )
        for tc in test_cases:
            f = open(tc['file_path'], "w")
            f.write(tc['sides'])
            f.close()
            self.assertEqual(tri_from_file(tc['file_path']), tc['type'])
            os.remove(tc['file_path'])

    def testIsoceles(self):
        test_cases = (
            {"file_path" : "iso1.txt",  "sides": "10 7 7", "type": "Isóceles"},
            {"file_path" : "iso2.txt", "sides": "4 5 4", "type": "Isóceles"},
        )
        for tc in test_cases:
            f = open(tc['file_path'], "w")
            f.write(tc['sides'])
            f.close()
            self.assertEqual(tri_from_file(tc['file_path']), tc['type'])
            os.remove(tc['file_path'])      

    
    def testEscaleno(self):
        test_cases = (
            {"file_path" : "esca1.txt",  "sides": "8 6 5", "type": "Escaleno"},
        )
        for tc in test_cases:
            f = open(tc['file_path'], "w")
            f.write(tc['sides'])
            f.close()
            self.assertEqual(tri_from_file(tc['file_path']), tc['type'])
            os.remove(tc['file_path'])  

if __name__ == "__main__":
    unittest.main()
