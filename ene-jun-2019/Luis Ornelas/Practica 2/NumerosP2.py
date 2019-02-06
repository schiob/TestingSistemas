def Calcular(numero):
    par = impar = negativo = positivo = 0
    for num in numero:
        if num % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if num > 0:
            positivo += 1
        elif num < 0:
            negativo += 1
    return (f"{positivo} Numero(s) Postivo(s)\n{negativo} Numeros Negativo(s)\n{par} Numero(s) Par(es)\n{impar} Numeors Impar(es)")

if __name__ == '__main__':
    print("Introduce Total de Numeros: ")
    num = input()
    print("Introduce los Numeros(Separados por un Espacio): ")
    numeros = input()
    numeros = list(map(int, numeros.split()))
    print(type((numeros)))
    print(Calcular(numeros))
