import pprint

class datos():

    def __init__(self,nombre,materia,cal,prom):
        self.nombre = nombre
        self.materia = materia
        self.calificacion = cal
        self.promedio = prom

    def __str__(self):

        return '''
			Nombre: {}\nMateria: {}\nCalificacion: {}\nPromedio: {}
		'''.format(self.nombre, self.materia, self.calificacion, self.promedio).strip()



    


def ReadGrades(file_name):

        file = open(file_name, "r")
        content = file.read()
        new = content.split("\n")
        #tama = len(new)
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
        
        return string
        #print(string)
        #for n in range(0,len(string)):    
        #    return datos(string[n]["nombre"],string[n]["materia"],string[n]["calificacion"],0)

def promedios(lista):
    
    dato  = lista
    nombre = dato[0]["nombre"]
    prom = 0
    suma = 0
    numcal = 0
    new_dic = {}

    for m,n in enumerate(dato):
        nombreL = dato[m]["nombre"]
        
        if nombre == nombreL:
            suma += dato[m]["calificacion"]
            numcal+=1
            m+=1
        else:
            nombre = nombreL
            suma += dato
        return suma
    




    #return promedios

if __name__ == "__main__":
    #pprint.pprint(ReadGrades("data.txt"))
    #ReadGrades("data.txt")
    #nombre  = datos(ReadGrades())
    item = ReadGrades("data.txt")
    #pprint.pprint(ReadGrades("data.txt"))

    pprint.pprint(promedios(item))
    
    