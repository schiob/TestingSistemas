import unittest
import os.path
import os
from archivos import IMCFile

class TestFiles(unittest.TestCase):
 
    def setUp(self):
      try: 
        file = open('c:/test/imc.txt') 
        file.close() 
        print ("El fichero existe")
      except: 
        print ("El fichero no existe")
        file = open('c:/test/imc.txt','w')
        file.close()
            

    def test_Human(self):
        Com = IMCFile(1.80, 73)
        self.assertEqual(Com, "22.53")
        

    def test_InHuman(self):
        Oli = IMCFile(3.40, 300)
        self.assertEqual(Oli, "25.95")
        

    def tearDown(self):
        
        os.remove('c:/test/imc.txt')


if __name__ == '__main__':
    
    unittest.main()
