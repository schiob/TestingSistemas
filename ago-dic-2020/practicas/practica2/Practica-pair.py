def validaciones(lista,actuales,deseados):
    listaCopia = list(lista)
    pantalonesAVender = listaCopia[:actuales-deseados]  #lista  de los n pantalones mas caros

    #######Verifica que te quedes con minimo un pantalon
    for i in pantalonesAVender:
        listaCopia.remove(i)
    for i in lista:
        if i not in listaCopia:
            return False

    ######Verifica que no sean mas de 5 marcas
    marcas = [i[0] for i in pantalonesAVender]
    numMarcas = {i: marcas.count(i) for i in marcas}
    for v in numMarcas.values():
        if v >= 5:
            return False

    return True


######
inputList = list(map(int,input().split()))
inputPantalones = []
actuales = inputList[0]
deseados = inputList[1]

for _ in range(actuales):
    inputPantalones.append(input().split(" "))

inputPantalones.sort(key= lambda x: int(x[1]), reverse=True )
print(inputPantalones)


if not validaciones(inputPantalones,actuales,deseados):
    print(0)
else:
    print( inputPantalones[:actuales-deseados].count(),sum(int(inputPantalones[:actuales-deseados][1])))