import unittest
from practica2 import escribir_archivo
from practica2 import imprimir_archivo

class TestUnitario(unittest.TestCase):
	#Función "contructor":
	def setUp(self):
		file = open("test2.txt", "w")

	#Funciones PrintFile:
	def test_print_file_1(self):
		escribir_archivo("test2.txt", "hola tacos")
		self.assertEqual(imprimir_archivo("test2.txt"), "hola tacos")

	def test_print_file_2(self):
		escribir_archivo("test2.txt", "")
		self.assertEqual(imprimir_archivo("test2.txt"), "")

	def test_print_file_3(self):
		escribir_archivo("test2.txt", "hola\nsalto\ntamal")
		self.assertEqual(imprimir_archivo("test2.txt"), "hola\nsalto\ntamal")	

	#Funciones WriteFile:
	def test_write_file_1(self):
		escribir_archivo("test3.txt", "charmander")
		self.assertEqual(imprimir_archivo("test3.txt"), "charmander")

	def test_write_file_2(self):
		escribir_archivo("test3.txt", "Ya es viernes")
		self.assertEqual(imprimir_archivo("test3.txt"), "Ya es viernes")
	

if __name__ == "__main__":
	unittest.main()