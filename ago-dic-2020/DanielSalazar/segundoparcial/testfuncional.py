import unittest
import csv
from calificacionesalumnos import separacionypromediacion
from os import remove

class TestCalificacionesAlumnos(unittest.TestCase):
    def setUp(self):
        valores=[['Jose_Lopez', 'quimica', 89.0], ['Jose_Lopez', 'matematicas', 85.34], ['Maria_Martinez', 'fisica', 95.5], ['Maria_Martinez', 'espanol', 90.0]]
        archivo="ejemplo_examen1.csv"
        csv=open(archivo,"w")
        titulor="<nombre_alumno> <materia> <calificacion>\n"
        csv.write(titulor)
        for alumno in valores:
            filas = alumno[0] + " " + alumno[1] + " " + str(alumno[2]) + "\n"
            csv.write(filas)
        csv.close()

        valores2=[]
        archivo2="ejemplo_examen2.csv"
        csv=open(archivo2,"w")
        csv.write(titulor)
        for alumno in valores2:
            filas = alumno[0] + " " + alumno[1] + " " + str(alumno[2]) + "\n"
            csv.write(filas)
        csv.close()

        valores3=[['Jose_Lopez', 'quimica', 89.0], ['Juan_Daniel', 'matematicas', 85.34], ['Maria_Martinez', 'espanol', 90.0]]
        archivo3="ejemplo_examen3.csv"
        csv=open(archivo3,"w")
        csv.write(titulor)
        for alumno in valores3:
            filas = alumno[0] + " " + alumno[1] + " " + str(alumno[2]) + "\n"
            csv.write(filas)
        csv.close()

        valores4=[['Jose_Lopez', 'quimica', 89.0]]
        archivo4="ejemplo_examen4.csv"
        csv=open(archivo4,"w")
        csv.write(titulor)
        for alumno in valores4:
            filas = alumno[0] + " " + alumno[1] + " " + str(alumno[2]) + "\n"
            csv.write(filas)
        csv.close()

        valores5=[['Juan_Daniel', 'quimica', 89.0], ['Juan_Daniel', 'matematicas', 85.34], ['Juan_Daniel', 'fisica', 95.5], ['Juan_Daniel', 'espanol', 90.0]]
        archivo5="ejemplo_examen5.csv"
        csv=open(archivo5,"w")
        csv.write(titulor)
        for alumno in valores5:
            filas = alumno[0] + " " + alumno[1] + " " + str(alumno[2]) + "\n"
            csv.write(filas)
        csv.close()

        valores6=[['Luis_Antonio', 'quimica', 89.0], ['Luis_Antonio', 'matematicas', 85.34], ['Luis_Antonio', 'fisica', 95.5], ['Perla_Marisol', 'espanol', 90.89], ['Perla_Marisol', 'ciencias_sociales', 75.42], ['Juan_Daniel', 'espanol', 70.005]]
        archivo6="ejemplo_examen6.csv"
        csv=open(archivo6,"w")
        csv.write(titulor)
        for alumno in valores6:
            filas = alumno[0] + " " + alumno[1] + " " + str(alumno[2]) + "\n"
            csv.write(filas)
        csv.close()

    def test_separacionypromediacion(self):
        salida_esperada = separacionypromediacion('ejemplo_examen1.csv')
        salida_real = [['Jose_Lopez', 87.17], ['Maria_Martinez', 92.75]]
        self.assertEqual(salida_real, salida_esperada)

        salida_esperada = separacionypromediacion('ejemplo_examen2.csv')
        salida_real = "El archivo no contiene ni una linea de datos"
        self.assertEqual(salida_real, salida_esperada)

        salida_esperada = separacionypromediacion('ejemplo_examen3.csv')
        salida_real = [['Jose_Lopez', 89.0], ['Juan_Daniel', 85.34], ['Maria_Martinez', 90.0]]
        self.assertEqual(salida_real, salida_esperada)

        salida_esperada = separacionypromediacion('ejemplo_examen4.csv')
        salida_real = [['Jose_Lopez', 89.0]]
        self.assertEqual(salida_real, salida_esperada)

        salida_esperada = separacionypromediacion('ejemplo_examen5.csv')
        salida_real = [['Juan_Daniel', 89.96]]
        self.assertEqual(salida_real, salida_esperada)

        salida_esperada = separacionypromediacion('ejemplo_examen6.csv')
        salida_real = [['Luis_Antonio', 89.95], ['Perla_Marisol', 83.16], ['Juan_Daniel', 70.0]]
        self.assertEqual(salida_real, salida_esperada)

    def tearDown(self):
        remove("ejemplo_examen1.csv")
        remove("ejemplo_examen2.csv")
        remove("ejemplo_examen3.csv")
        remove("ejemplo_examen4.csv")
        remove("ejemplo_examen5.csv")
        remove("ejemplo_examen6.csv")


if __name__ == '__main__':
    unittest.main()