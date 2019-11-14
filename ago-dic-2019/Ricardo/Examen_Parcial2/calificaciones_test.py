import unittest
import calificaciones
class test(unittest.TestCase):
	def test1(self):
		archivo = 'materias.txt'
		self.assertEqual(calificaciones.materias_alumno(archivo),'''
        Jose_Lopez 87.17
        Maria_Martinez 92.75
        ''')