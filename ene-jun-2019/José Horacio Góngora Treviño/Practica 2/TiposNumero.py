def tipos_numeros(numeros):
    pos = 0
    neg = 0
    par = 0
    impar = 0
    for i in numeros:
        if i > 0:
            pos+=1
        if i < 0:
            neg+=1
        if i % 2 == 0 or i == 0:
            par+=1
        if i % 2 !=0:
            impar+=1
    return (f"{pos} número(s) positivo(s)\n{neg} número(s) negativo(s)\n{par} número(s) par(es)\n{impar} número(s) impar(es)")

if __name__ == '__main__':
    print("Introduce cuantos numeros quieres ordenar")
    n = input()
    print("Introduce los numeros deseados separados por un espacio")
    numeros = input()
    numeros = list(map(int, numeros.split()))
    print(tipos_numeros(numeros))