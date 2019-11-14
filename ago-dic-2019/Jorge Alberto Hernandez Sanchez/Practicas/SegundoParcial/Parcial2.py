import unittest
from unittest.mock import Mock, patch


alumnos = []
archivo = open("C:\\Users\\jorge\\Documents\\Cursos\\TestingSistemas\\ago-dic-2019\\Jorge Alberto Hernandez Sanchez\\Practicas\\SegundoParcial\\Calificaciones.txt", 'r')
datos = archivo.readline()
separador = datos.split(",")
archivo.close()

print(separador)
def Calificaciones(list):
    dato_uno = separador[0]
    sep1 = dato_uno.split(" ")
    dato_dos = separador[1]
    sep2 = dato_dos.split(" ")
    dato_tres = separador[2]
    sep3 = dato_tres.split(" ")
    dato_cuatro = separador[3]
    sep4 = dato_cuatro.split(" ")

    promedio1 = (float(sep1[2]) + float(sep2[2]))/2
    promedio2 = (float(sep3[2]) + float(sep4[2]))/2

    return "{} {} \n{} {}".format(sep1[0], promedio1, sep3[0], promedio2)
Calificaciones(separador)

Alumnos = ['Jose_Lopez quimica 89.00', 'Jose_Lopez matematicas 85.34', 'Maria_Martinez fisica 95.50', 'Maria_Martinez espaÃ±ol 90.00']
class Test_Calificaciones(unittest.TestCase):
    @patch('builtins.open')
    def test_calificaciones(self, mock_open):
        for r in range(len(Alumnos)):
            mock_open.return_value.read.return_value = Alumnos[r]
            res = Calificaciones(mock_open)
            resultado = Calificaciones(separador)
            self.assertEqual(res, resultado)

if __name__ == '__main__':
    unittest.main()