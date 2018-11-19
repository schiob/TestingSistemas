def calc(cantidad):
    impares = 0 
    pares = 0
    negativos = 0
    positivos = 0
    for num in cantidad:
        if num%2==0:
            pares+=1
        else:
            impares+=1
        if num<0:
            negativos+=1
        elif num>0:
            positivos+=1
    return pares, impares, negativos, positivos

if __name__ == '__main__':
    numero=int(input('Escribe el total de números para evaluar: '))
    cantidad=list(map(int,input('Escribe los números a evaluar (separados con un espacio entre ellos): ').split(" ")))
    resultado=calc(cantidad)

    print("Numeros pares = {}".format(resultado[0]))
    print("Numeros impares = {}".format(resultado[1]))
    print("Numeros negativos = {}".format(resultado[2]))
    print("Numeros positivos = {}".format(resultado[3]))