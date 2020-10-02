def MergeSort(lista):
    if len(lista) > 1:
        mitad = len(lista)//2
        Izq = lista[:mitad]
        Der = lista[mitad:]
        MergeSort(Izq)
        MergeSort(Der)
        i=0 
        j=0
        k=0
        while i < len(Izq) and j < len(Der):
            if int(Izq[i][1]) < int(Der[j][1]):
                lista[k] = Izq[i]
                i+=1
            else: 
                lista[k] = Der[j]
                j+=1
            k+=1

        while i < len(Izq):
            lista[k] = Izq[i]
            i+=1
            k+=1
        while j < len(Der):
            lista[k] = Der[j]
            j+=1
            k+=1
lista = []
lista2= []
n,x = map(int,input().strip().split(" "))
if n>x:
  for i in range(n):
    panta= input("Pantalones: ").split()
    lista.append(panta)
    lista2.append(panta)
  MergeSort(lista)
  MergeSort(lista2)
  extrae=(lista.pop(4) + lista.pop(4)+ lista.pop(5))
  num=(lista.pop(0),lista.pop(1),lista.pop(2))
  extrae2=(lista2.pop(4) + lista2.pop(4)+ lista2.pop(5))
  precio=(int(extrae2.pop(1))+int(extrae2.pop(2))+int(extrae2.pop(3)))
  print(len(num),precio)

else:
  print(0)
