import unittest
from primer_parcial import triangulo_desde_archivo

class TestUnitario(unittest.TestCase):
	#Función "constructor":
	def setUp(self):
		equi_1 = open("equi_1.txt", "w")
		equi_1.write("3 3 3")
		equi_1.close()

		equi_2 = open("equi_2.txt", "w")
		equi_2.write("5 5 5")
		equi_2.close()

		noTri_1 = open("noTri_1.txt", "w")
		noTri_1.write("0 0 0")
		noTri_1.close()

		noTri_2 = open("noTri_2.txt", "w")
		noTri_2.write("0 5 7")
		noTri_2.close()

		noTri_3 = open("noTri_3.txt", "w")
		noTri_3.write("1 2 3")
		noTri_3.close()

		iso_1 = open("iso_1.txt", "w")
		iso_1.write("10 7 7")
		iso_1.close()

		iso_2 = open("iso_2.txt", "w")
		iso_2.write("4 5 4")
		iso_2.close()

		esc_1 = open("esc_1.txt", "w")
		esc_1.write("8 6 5")
		esc_1.close()

	#Funciones test:
	def test_equilatero(self):
		self.assertEqual(triangulo_desde_archivo("equi_1.txt"), "Equilátero.")
		self.assertEqual(triangulo_desde_archivo("equi_2.txt"), "Equilátero.")

	def test_no_triangulo(self):
		self.assertEqual(triangulo_desde_archivo("noTri_1.txt"), "No es triangulo.")
		self.assertEqual(triangulo_desde_archivo("noTri_2.txt"), "No es triangulo.")
		self.assertEqual(triangulo_desde_archivo("noTri_3.txt"), "No es triangulo.")

	def test_isoceles(self):
		self.assertEqual(triangulo_desde_archivo("iso_1.txt"), "Isóceles.")
		self.assertEqual(triangulo_desde_archivo("iso_2.txt"), "Isóceles.")

	def test_escaleno(self):
		self.assertEqual(triangulo_desde_archivo("esc_1.txt"), "Escaleno.")

if __name__ == '__main__':
	unittest.main()