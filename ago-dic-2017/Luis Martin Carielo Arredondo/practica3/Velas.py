def birthdaycake_candles(n,lista):
    m=0
    mayor=0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    for i in range(n):
        if lista[i]==mayor:
            m+=1
    return m

if __name__ == '__main__':
    n=int(input("Ingresa el número de velas: "))
    lista=[]
    for i in range(n):
        num=int(input("Ingrese el valor: "))
        lista.append(num)
    result=birthdaycake_candles(n,lista)
    print(result)