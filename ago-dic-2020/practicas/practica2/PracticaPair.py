import collections

#####
def validar1(lista):
    for i in range (0,len(lista)):
        if  lista[i] == 1:  
            print("No puedes vender todos los pantalones de una marca")

            return False
        else:
            return True

def validar5(lista):
    for i in range (0,len(lista)):
        if lista[i] >= 5:
            print("No puedes vender mas de 5 pantalones de una marca")

            return False
        else:
            return True


def validaciones(lista):
    pantalonesAVender = list(lista)
    Listamarcas=[]
    for i in pantalonesAVender:
        Listamarcas.append(i[0])

    dicmar = collections.Counter(Listamarcas)
    valpan=list(dicmar.values())
    pasar = validar1(valpan)

    ######Verifica que no sean mas de 5 de la misma marca
    pasar = validar5(valpan)
    return pasar


###############################
 



def PedirTotales(inputList):
    ######
    N = inputList[0]
    X = inputList[1]
    return N,X


def CrearListaPantalones(N):  
    inputPantalones = [] 
    for i in range(N):
      try:
        arr = input("Marca y Precio del Pantalon\n").split()
        arr[1] = int(arr[1])
      except Exception:
          print("Solo se permite introducir numero en el precio")

    inputPantalones.sort(key= lambda k: (k[1]), reverse=True )
    return inputPantalones
inputList=[] 

try:
    inputList = list(map(int,input("Cuantos pantalones tienes y cuantos quieres vender?\n").split()))
except Exception:
    print("Solo se permite introducir numeros")



N,X = PedirTotales(inputList)
listapantalones = CrearListaPantalones(N)

if validaciones(listapantalones)== False:
    print(0)
else:
    suma = 0
    for i in listapantalones[:N-X]:
        suma += i[1]
        count= N-X
    
    print(count, suma)
