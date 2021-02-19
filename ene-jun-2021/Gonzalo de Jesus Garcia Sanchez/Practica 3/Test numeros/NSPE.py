#   51 -12 -3 0 2
#   Gonchologon
def practica1(lista):
    pares, impares, positivo, negativo = 0, 0, 0, 0 #CREAMOS UN CONTADOS DE PAR IMPAR POSI NEGAT INICIALIZANDOLOS EN 0
   
    for n in lista: #Pasamos por cada numero que hay en la lista
        if n >0:            #POSOTIVO
            positivo += 1
        if n < 0:           #NEGATIVO
            negativo += 1
        if n % 2 == 0 or n == 0:     #PARES
            pares += 1
        else:               #IMPARES
             impares += 1
    return (f"{positivo} número positivo\n{negativo} número negativo\n{pares} número par\n{impares} número impar") #RETORNAMOS LA LISTA PRIMER LUGAR PARES 2DO IMPARE ETC ETC

if __name__ == '__main__':
    n = input("Introduce cuantos numeros quieres ordenar: ")
    lista = input("Introduce los numeros deseados separados por un espacio: ")
    lista = list(map(int,lista.split()))
    print(practica1(lista))