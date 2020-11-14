class Alumno():
    def __init__(self,datos):
        self.datos = datos
        
    def __str__(self):
        return "{}".format(self.datos)
    
    #comparacion de datos
    
    def __eq__(self,datos):
        if datos.datos != self.datos:
            return False
        return True
    
class Archivo():
    def __init__(self,archivo):
        self.archivo = open(archivo,'a')
        self.archivo.close()
    #funcion para guardar alumno
    def alumno(self,datos):
        f = open("datosAlumno.txt","a") #abrir archivo para anadir dato
        f.write(datos.datos)
        f.close()
        #SALIDA DE DATOS
    def salida(self):
        f=open("datosAlumno.txt","r")
        print(f.read())
#AGREGA A UN NUEVO ALUMNO se necesita llamar a la funcion alumno de archivo
def AgregaAlumno(alumno,archivo):
    archivo.alumno(alumno)
#NOS DEVUELVE LOS ALUMNOS EXITENTES
def muestralumnos(archivo):
    alumnos=archivo.salida()
    return alumnos
    
if __name__ == "__main__":
    alumno1 = Alumno("\nJose_Lopez quimica 89.00")
    alumno2 = Alumno ("\nJose_Lopez matematicas 85.34")
    #llamamos a nuestro archivo para agregarlos
    archivo = Archivo("datosAlumno.txt")
        
    AgregaAlumno(alumno1,archivo)
    AgregaAlumno(alumno2,archivo)
    print(muestralumnos(archivo))