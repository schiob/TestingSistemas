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
        
        IMCFile(1.80, 73)
        file = open("c:/test/imc.txt","r")
        mensaje = file.read()
        self.assertEqual(mensaje, "22.53")
        file.close()

    def test_InHuman(self):
        IMCFile(3.40, 300)
        file = open("c:/test/imc.txt","r")
        mensaje = file.read()
        self.assertEqual(Oli, "25.95")
        file.close()

    def tearDown(self):
        
        os.remove('c:/test/imc.txt')


if __name__ == '__main__':
    
    unittest.main()
