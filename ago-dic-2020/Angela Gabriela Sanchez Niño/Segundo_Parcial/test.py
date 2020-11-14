import unittest
import os #libreria que nos permite aceder a funcionalidades dependientesdel sistema
from unittest.mock import MagicMock
#importa clases y funcion
from app import muestralumnos,Alumno,Archivo
#se crear la clase para testear datos
class TestAlumno(unittest.TestCase):
    def setUp(self):
        self.archivo = Archivo ("datosAlumno.txt")
        self.archivo.alumno(Alumno("\nJose_Lopez quimica 89.00"))
        #self.archivo.AgregaAlumno(Alumno("Jose_Lopez", "matematicas", 85.34))
        
    #eliminar datos  
    def Baja(self):
        os.remove("datosAlumno.txt")
        
    #funcion para testear datos
    def Mostrar(self):
        entrada = "Jose_Lopez quimica 89.00 \n Jose_Lopez 89.00"
        salida_esperada = "Jose_Lopez quimica 89.00 \n Jose_Lopez 89.00 "
        
        
        #se realiza el mock para pruebas unitarias
        #simulando archivo
        Mock = MagicMock()
        Mock.salida.return_value = entrada
        salida_actual = muestralumnos(Mock)
        #se comparan datos
        self.assertEqual(salida_actual,salida_real)
        
    #FUNCION DE INTEGRACION
    #para probar pruebas unitarias comentar esta funcion
    def test_integracion(self):
        salida_actual = "Jose_Lopez quimica 89.00"
        salida_real = muestralumnos(self.archivo)
        self.assertEqual(salida_actual,salida_real)
if __name__ == "__main__":
    unittest.main()
    