import pandas

def conseguirdatos(archivocsv):
    #aquí solamente se asigna a un objeto el contenido del archivo
    archivo = pandas.read_csv(archivocsv)
    
    #aquí se toman solo los valores del archivo
    datos = archivo.values.tolist()
    #aquí se toman los valores que vamos a usar, se parten por el @ los correos y se toma solo el dominio
    #y los puntos, excluimos el nombre por que no lo vamos a necesitars
    datos = [[i[1].split("@")[1], int(i[2])] for i in datos]

    return datos

def separacionypromediacion():

    datazos = conseguirdatos('ejemplo.csv')
    #aquí es donde se van a guardar los promedios de cada dominio
    valoresfinales = []

    #esto se va a realizar hasta que en datazos ya no haya nada, osea ya no queden valores ni nada
    while len(datazos) > 0:
        #inicializamos las variables que vamos a utilizar
        dominios = []
        indices = []
        #se toma el primer valor que queda en la lista
        ultimodom = datazos[0][0]
        #se siguen inicializando variales que utilizaremos
        indice = 0
        contador = 0
        sumatoria = 0

        #en este ciclo asignamos a una lista de listas los dominios, se van separando conforme dominios y
        #los indices se utilizan para saber en que lugar estaban los valores que ya no vamos a utilizar
        #y poder popearlos después, digamos que se hace una lista de listas con los puros dominios de hotmail,
        #pues como ya los guardamos en otro lado ahora los borramos de la lista principal
        for d in datazos:
            dominio, puntos = d[0], d[1]
            if ultimodom == dominio:
                dominios.append([dominio, puntos])
                indices.append(indice)
            indice +=1
        
        #aquí se borran los valores que ya utilizamos haciendo uso de los indices
        while contador < len(indices):
            datazos.pop(indices[contador] - contador)
            contador += 1
        
        #se suman los puntos de el dominio que se este utilizando
        for i in dominios:
            sumatoria += i[1]
        
        #se asigna el dominio que se utilizo y se saca su promedio entre todos los puntos de las personas que
        #utilizaban aquel dominio
        valores = [dominios[0][0], sumatoria/len(dominios)]

        #se guardan los valores en la lista final, aquí ira solo el dominio y el promedio de todos los que
        #tenian ese dominio
        valoresfinales.append(valores)

    return valoresfinales

if __name__ == "__main__":
    dominiosypromedios = separacionypromediacion()
    print(dominiosypromedios)
    
