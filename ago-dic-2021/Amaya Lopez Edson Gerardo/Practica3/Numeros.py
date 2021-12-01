lista=[]
def numero(lista):
    par=0
    impar=0
    positivo=0
    negativo=0

    for n in lista:
        if n % 2 == 0:
            par+=1
        else:
            impar +=1
        if n < 0:
            negativo = negativo + 1
        elif n>0:
            positivo+=1
    return (f'{positivo} numero positivo\n{negativo} numero negativo\n{par} numero par\n{impar} numero impar')



if __name__ == "name":

    num=int(input('cantidad de elementos'))
    for n in range(num):
        entrada = int(input(f'numero {n+1}: '))
        lista.append(entrada)



