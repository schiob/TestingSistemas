import os
import unittest
import tempfile

from practica2 import printFile
from practica2 import writeFile

class testPractica2(unittest.TestCase):
    
    #archivo para probar string 'hola tacos'	
	taco = open('./holatacos.txt','w')
	taco.write('hola tacos')
	taco.close()
	
    #archivo para probar contenido vacío
	vacio = open('vacio.txt','w')
	vacio.write('')
	vacio.close()
	
    #archivo para probar "hola\nsalto\ntamal"
	salto = open('salto.txt','w')
	salto.write('hola\nsalto\ntamal')
	salto.close()
	
    #archivo para probar path nuevo.
	nuevo = open('./nuevo.txt','w')
	nuevo.write('Este es un texto')
	nuevo.close()	
		
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
