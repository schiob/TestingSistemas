
def birthdayCakeCandles(lista):
    m=0
    mayor=0
    
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    for i in range(len(lista)):
        if lista[i]==mayor:
            m+=1

   
    resultado= m
    return resultado








