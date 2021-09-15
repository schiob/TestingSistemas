def juanitaList(lista):

    pos = 0
    neg = 0
    par = 0
    imp = 0
    for numero in lista:

        if numero > 0:
            pos = pos + 1
            if numero % 2 == 0:
                par = par + 1
            else:
                imp = imp + 1
        elif numero < 0:
            neg = neg + 1
            if numero % 2 == 0:
                par = par + 1
            else:
                imp = imp + 1
        elif numero == 0:
            par = par + 1

    return(f'{pos} número(s) positivo(s)\n{neg} número(s) negativo(s)\n{par} número(s) par(es)\n{imp} número(s) impar(es)')


if __name__ == '__main__':
    lista = []

    num = int(input('¿Cuantos numero debe llevar la lista Juanita:)? '))
    for i in range(num):
        numero = int(input(f'Ingrese el numero: {i} '))
        lista.append(numero)

    print(juanitaList(lista))
