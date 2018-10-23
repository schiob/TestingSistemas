def Sumar(x,y):
    suma=0
    if x>y:
        for i in range(y+1,x):
            if i%2:
                suma+=i

    for i in range(x+1,y-1):
        if i%2:
            suma+=i
    return suma

if __name__ == '__main__':
    x=int(input("Ingrese numero: "))
    y=int(input("Ingrese numero: "))
    resultado=Sumar(x,y)
    print("Suma = {}".format(resultado))
