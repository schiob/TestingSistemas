import unittest
import Practica4
from unittest.mock import patch

def leerarchivo(archivo):
	archivo = open(archivo,'r+')
	arch=archivo.read()
	texto=''
	#arch.lower()
	#arch=re.compile(r'\W+', re.UNICODE).split(arch)
	for i in range(len(arch)):
		if arch[i].isalnum() or arch[i].isalpha() or arch[i].isdigit() or arch[i] == ' ' or arch[i] == '\n':
			#arch[i].lower()
			if arch[i] != '':
				texto=texto+arch[i]
	texto = texto.lower()
	return texto

def Funcion_Mock(self):
	return 'texto1'

class test(unittest.TestCase):
	def test1_modifica(self):
		archivo = 'practica4.txt'
		self.assertEqual(Practica4.leerarchivo(archivo),'hola esto es una prueba')
	def test2_vacio(self):
		archivo='practica4_2.txt'
		self.assertEqual(Practica4.leerarchivo(archivo),'')
	def test3(self):
		archivo='practica4_3.txt'
		self.assertEqual(Practica4.leerarchivo(archivo),'hola esto es una prueba')

	@patch('builtins.open')
	def test_mock(self,mock_open):
		mock_open.return_value.read.return_value = 'dialogo'
		archi=Practica4.leerarchivo('practica4.txt')
		self.assertEqual(archi,'dialogo')

if __name__ == "__main__":
	unittest.main()
