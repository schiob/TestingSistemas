def  clasif(numeros):
    conteoImpar = conteoPar = conteoPositivos = conteoNegativos = 0

    for i in numeros:
        if i % 2:
            conteoImpar += 1
        else:
            conteoPar+=1

    for i in numeros:
        if i==0:
            i += 1
        else:
            if i>0 and i != 0:
                conteoPositivos+=1
            else:
                conteoNegativos+=1

    return conteoPositivos, conteoNegativos, conteoPar, conteoImpar

if __name__=='__main__':

    n = int(input())
    lista=list(int, input().split(' '))


    print("%d número(s) positivo(s)" % conteoPositivos)
    print("%d número(s) negativo(s)" % conteoNegativos)
    print("%d número(s) par(es)" % conteoPar)
    print("%d número(s) impar(es)" % conteoImpar)
