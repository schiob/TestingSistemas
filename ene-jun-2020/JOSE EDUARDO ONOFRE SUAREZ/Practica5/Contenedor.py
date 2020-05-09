
class contenedor:

    def volumencontenedor(lista1,lista2):

        listaC = []
        suma = 0
        for i in range(0,len(lista1)):
            listaC.append(lista1[i]*lista2[i])

        for i in range(0,len(listaC)):
            suma+= listaC[i]

        return suma




if __name__ == "__main__":
    
    n = int(input("Escriba el numero de contenedores a usar:"))
    contenedores = []
    volumenes = []
    for i in range(0,n):
        contenedores.append(int(input("Escriba el numero de contenedores de la posicion {}:".format(i+1))))
        volumenes.append(int(input("Escriba el volumen del contenedor en la posicion {}:".format(i+1))))
    
    #print(contenedores)

    print("-----Mostrando el resultado-----\n")
    print(contenedor.volumencontenedor(contenedores,volumenes))
