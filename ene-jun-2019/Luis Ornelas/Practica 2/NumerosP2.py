def Calcular(numeros):
    par = impar = negativo = positivo = 0
    for num in numeros:
        if num % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if num > 0:
            positivo += 1
        elif num < 0:
            negativo += 1
    return "{} Numero(s) Positivo(s)\n{} Numero(s) Negativo(s)\n{} Numero(s) Par(es)\n{} Numero(s) Impar(es)".format(positivo,negativo,par,impar)

if __name__ == '__main__':
    print("Introduce Total de Numeros: ")
    num = input()
    print("Introduce Los Numeros(Separados por un Espacio): ")
    numeros = input()
    numeros = list(map(int, numeros.split()))
    print(type((numeros)))
    print(Calcular(numeros))
