from abc import ABC,abstractclassmethod


class alumno():
    def __init__(self,nombre,materia,cal,prom):
        self._nombre = nombre
        self._materia = materia
        self._calificacion = cal
        self._promedio = prom

class Promedio(ABC):
    @abstractclassmethod
    def Search(nombre):
        pass

def getAverage(nombre,arch):
    alumno = arch.Search(nombre)

    return alumno.promedio

class DBread(Promedio):
    
    def __init__(self, file_name):
        self._archivo = archivo


    def ReadGrades(self):

        file = open(file_name, "r")
        content = file.read()
        new = content.split()
        file.close()

        string = []
        lista = []

        for i in new:
            lista.append(i.split())

        for i,x in enumerate(lista):
            stud = {

                "nombre" : lista[i][0], 
                "materia" : lista[i][1],
                "calificacion" : float(lista[i][2])

            }
            string.append(stud)
            
        for i in string:

            return alumno(string[i]["nombre"],string[i]["materia"],string[i]['calificacion'],0)

#def TakeData():


if __name__ == "__main__":
    archivo = dBread("data.txt")
    print(getAverage("Jose_Lopez",archivo)
