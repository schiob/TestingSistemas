def lista(numero):
    positivo=0
    negativo=0
    par=0
    impar=0
    for i in numero:
        if i >0:
            positivo=positivo+1
            if i %2==0:
                par=par+1
            else:
                impar= impar+1
        else:
            negativo=negativo+1
            if i == 0:
                negativo=negativo-1
            if i %2==0:
                par=par+1
            else:
                impar= impar+1

    return (f'Numeros positivos:\n{positivo}\nNumeros negativos:\n{negativo}\nNumeros pares:\n{par}\nNumeros impares:\n{impar}')

if __name__=="__main__":
    n=int(input("..."))
    numero=list(int(input("....")) for i in range(n))
    #numero=[0]
    print(lista(numero))