import csv

def calcular_promedio():
    lista = open("ago-dic-2021\Diaz Delabra Erick\Parcial 2\calificaciones.txt") #lista original
    contLista = csv.reader(lista, delimiter=" ")
    lista2 = [] 
    listaResultados = []
    for i in contLista:
        lista2.append("{} {} {}".format(i[0], i[1], i[2])) #lista 2 guarda la lista original ordenada para el otro for
    cont= 0
    promedio = 0
    for i in lista2:
        x = str(i)
        alumno = x.split(' ') #separamos por coma los alumnos de la lista 2
        nombreA = alumno[0]
        califA = alumno[2] #guardamos los datos sin que se guarde la materia
        promedio += float(califA)
        cont += 1 #el contador nos sirve para no sumarr mas de las 2 calificaciones del alumno y no amontonarnos con el siguiente
        if (cont == 2): 
            listaResultados.append("{} {}".format(nombreA, promedio / 2)) #guardamos el nombre con el promedio
            cont = 0
            promedio = 0

    return listaResultados

if __name__ == '__main__':
    print(calcular_promedio())
