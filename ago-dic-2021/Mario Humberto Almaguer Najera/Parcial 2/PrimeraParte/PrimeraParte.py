import csv

class PrimeraParte:

    def leer_archivo(self):
        contador = 0
        suma = 0
        archivo = open('PrimeraParte/datos.txt')
        leer = csv.reader(archivo, delimiter=" ")
        alumnos = []
        resultados = []
        for linea in leer:
            nombre = linea[0]
            if len(linea) > 2:
                alumnos.append('{} {} {}'.format(linea[0], linea[1], linea[2]))
            else:
                return 'No hay columna calificacion en el archivo'

        # Sumar promedios del mismo nombre
        for i in alumnos:
            actual = str(i)
            alumno = actual.split(' ')
            nombreAlumno = alumno[0]
            
            if nombreAlumno == '':
                return 'No hay columna nombre en el archivo'

            califAlumno = float(alumno[2])
            suma += califAlumno
            contador += 1
            if (contador == 2):
                resultados.append('{} {}'.format(nombreAlumno, suma / contador))
                contador = 0
                suma = 0

        return resultados


if __name__ == '__main__':
    pp = PrimeraParte()
    print(pp.leer_archivo())