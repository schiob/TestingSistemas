import collections

#####
def validaciones(lista):
    pantalonesAVender = list(lista)
    Listamarcas=[]
    for i in pantalonesAVender:
        Listamarcas.append(i[0])

    dicmar = collections.Counter(Listamarcas)
    valpan=list(dicmar.values())
    i=0
    for i in range (0,len(valpan)):
        if  valpan[i] == 1:  
            print("No puedes vender todos los pantalones de una marca")

            return False
   
    ######Verifica que no sean mas de 5 de la misma marca
    for i in range (0,len(valpan)):
        if valpan[i] >= 5:
            print("No puedes vender mas de 5 pantalones de una marca")

            return False

    return True


######
inputList = list(map(int,input("Cuantos pantalones tienes y cuantos quieres vender?\n").split()))
inputPantalones = []
N = inputList[0]
X = inputList[1]

for i in range(N):
    arr = input("Marca y Precio del Pantalon\n").split()
    arr[1] = int(arr[1])
    inputPantalones.append(arr)

inputPantalones.sort(key= lambda k: (k[1]), reverse=True )
#listas = ["dasdw","dasdw","dasw"]
#print(collections.Counter(listas))
#print(inputPantalones[:N-X][1])
#print("hola")
if validaciones(inputPantalones)== False:
    print(0)
else:
    suma = 0
    for i in inputPantalones[:N-X]:
        suma += i[1]
        count= N-X
    
    print(count, suma)
