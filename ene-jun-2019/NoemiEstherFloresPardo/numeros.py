def tipos_numeros(numeros):
    par = 0
    impar = 0
    positivo = 0
    negativo = 0
    for cont in numeros:
        if cont > 0:
            positivo = positivo + 1
        if cont < 0:
            negativo = negativo + 1
        if cont % 2 == 0 or cont == 0:
            par = par + 1
        if cont % 2 !=0:
            impar = impar + 1
    return (f"{positivo} número(s) positivo(s)\n{negativo} número(s) negativo(s)\n{par} número(s) par(es)\n{impar} número(s) impar(es)")
if __name__ == '__main__':
    print("¿Cuántos números son?")
    n = input()
    print("Ingresa números")
    numeros = input()
    numeros = list(map(int, numeros.split()))
    print(type((numeros)))
    print(tipos_numeros(numeros))