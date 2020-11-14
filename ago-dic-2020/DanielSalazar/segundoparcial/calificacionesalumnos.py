import pandas

def separacionypromediacion(archivocsv):
    archivo = pandas.read_csv(archivocsv, sep=' ')

    datos = archivo.values.tolist()

    if len(datos) < 1:
        return "El archivo no contiene ni una linea de datos"

    datazos = [[i[0], float(i[2])] for i in datos]

    #aquí es donde se van a guardar los promedios de cada alumno
    valoresfinales = []

    #esto se va a realizar hasta que en datazos ya no haya nada, osea ya no queden valores ni nada
    while len(datazos) > 0:
        #inicializamos las variables que vamos a utilizar
        nombres = []
        indices = []
        #se toma el primer valor que queda en la lista
        ultimonombre = datazos[0][0]
        #se siguen inicializando variales que utilizaremos
        indice = 0
        contador = 0
        sumatoria = 0

        #en este ciclo asignamos a una lista de listas los nombres, se van separando conforme alumno y
        #los indices se utilizan para saber en que lugar estaban los valores que ya no vamos a utilizar
        #y poder popearlos después, digamos que se hace una lista de listas con los puros nombres de alumnos,
        #pues como ya los guardamos en otro lado ahora los borramos de la lista principal
        for d in datazos:
            nombre, calificacion = d[0], d[1]
            if ultimonombre == nombre:
                nombres.append([nombre, calificacion])
                indices.append(indice)
            indice +=1
        
        
        #aquí se borran los valores que ya utilizamos haciendo uso de los indices
        while contador < len(indices):
            datazos.pop(indices[contador] - contador)
            contador += 1
        
        #se suman las calificaciones de el alumno que se este utilizando
        for i in nombres:
            sumatoria += i[1]
        
        #se asigna el alumno que se utilizo y se saca el promedio entre todas las calificaciones del alumno
        valores = [nombres[0][0], round(sumatoria/len(nombres), 2)]

        #se guardan los valores en la lista final, aquí ira solo el nombre y el promedio de cada alumno
        valoresfinales.append(valores)

    return valoresfinales

def main():
    nombresypromedios = separacionypromediacion('ejemplo_examen.csv')
    
    if nombresypromedios == "El archivo no contiene ni una linea de datos":
        print (nombresypromedios)
    else:
        for alumno in nombresypromedios:
            calificacion = alumno[0] + " " +str(alumno[1])
            print(calificacion)

if __name__ == "__main__":
    main()