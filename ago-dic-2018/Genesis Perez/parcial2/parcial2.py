def sumaimpares(rango):
    suma=0
    numero1=rango[0]
    numero2=rango[1]

    if numero1<numero2:
        for i in range(numero1+1,numero2-1):
            if i % 2:
                suma+=i

    for i in range(numero2+1,numero1):
        if i % 2:
            suma+=i
    return suma

if __name__=='__main__':
    xy=[int(i) for i in (input("Ingresa los numeros: ").split(' '))]
    resultado = sumaimpares(xy)
    print("La suma es: ")
    print("{}".format(resultado))
