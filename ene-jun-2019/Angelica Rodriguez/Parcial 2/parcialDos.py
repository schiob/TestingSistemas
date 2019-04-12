
class Alumno():

    def __init__(self, datosAlumno):
        self.datosAlumno = datosAlumno

    def __str__(self):
        return "{}".format(self.datosAlumno)

    # compara cada atributo de la mascota para saber si son iguales
    def __eq__(self, datosAlumno):
        if datosAlumno.datosAlumno != self.datosAlumno:
            return False
        return True

class Archivo():
    def __init__(self, archivo):
        self.archivo = open(archivo, 'a')
        self.archivo.close()

    def guardarAlumno(self, datosAlumno):
        f = open("datosAlumnos.txt", "a")
        f.write(datosAlumno.datosAlumno+"\n")
        f.close()

    def getSalida(self):
        f = open("datosAlumnos.txt", "r")
        print(f.read())

# método para guardar mascotas
def saveAlumno(alumno, archivo):
    archivo.guardarAlumno(alumno)

# método para mostrar todas las mascotas
def showAlumnos(archivo):
    alumnos = archivo.getSalida()
#    calificaciones = 0
#    for line in f:
#        if(nombre == nombre2):
#            sum += 1
#        nombre, materia, calificacion = list(map(str, line.strip().split()))
#        nombre2 = nombre
#        calificaciones += float(calificacion)

    print(sum)
    return alumnos

if __name__ == "__main__":
    # creación de tres mascotas
    alumno1 = Alumno("Jose_Lopez quimica 89.00")
    alumno2 = Alumno("Jose_Lopez matematicas 85.34")

    archivo = Archivo("datosAlumnos.txt")

    saveAlumno(alumno1, archivo)
    saveAlumno(alumno2, archivo)
    print(showAlumnos(archivo))
