import os
import unittest
import tempfile

from practica2 import printFile
from practica2 import writeFile

class testPractica2(unittest.TestCase):
    
    
    def setUp(self):        
        #archivo para probar string 'hola tacos'    
        self.taco = open('./holatacos.txt','w')
        self.taco.write('hola tacos')
        self.taco.close()
        
        #archivo para probar contenido vacío
        self.vacio = open('vacio.txt','w')
        self.vacio.write('')
        self.vacio.close()
        
        #archivo para probar "hola\nsalto\ntamal"
        self.salto = open('salto.txt','w')
        self.salto.write('hola\nsalto\ntamal')
        self.salto.close()
        
        #archivo para probar path nuevo.
        self.nuevo = open('./nuevo.txt','w')
        self.nuevo.write('Este es un texto')
        self.nuevo.close()   
        
        
    def testHolaTacos(self):
        self.assertEqual(printFile(self.taco.name),"hola tacos")
        
    def testVacio(self):
        self.assertEqual(printFile(self.vacio.name),'')
    
    def testSalto(self):
        self.assertEqual(printFile(self.salto.name),'hola\nsalto\ntamal')
    
    def testSobreEscrituraArchivoNuevo(self):       
        self.assertEqual(writeFile(self.nuevo.name,'Charmander'),'Charmander')
        
    def testSobreEscrituraArchivoExistente(self):
        self.assertEqual(writeFile(self.nuevo.name,'Ya es viernes'),'Ya es viernes')
    
    
        
        
if __name__ == '__main__':
    unittest.main()
