def limite_censura(palabras, texto, palabra_cambio, diferencia):
    palabras = palabras.split(' ')
    t_inicial = len(texto)

    for i in palabras:
        texto = texto.replace(i, palabra_cambio)

    suma = t_inicial + diferencia
    resta = t_inicial - diferencia

    if t_inicial == len(texto):
        return 'Es una cadena valida'
    elif resta <= len(texto) <= suma:
        return 'Es una cadena valida'
    else:
        return 'No es una cadena valida'


def censura(palabras, texto, palabra_cambio):
    palabras = palabras.split(' ')

    for i in palabras:
        texto = texto.replace(i, palabra_cambio)

    return texto


def main():
    salir = False

    while not salir:
        opc = int(input('Elige una funcion a realizar\n1 -> Censurar unas palabras.\n2 -> Limite de tamaño de censura.\n3 -> Salir\nOpcion -> '))

        if opc == 1:
            pal = input('Dame una lista de las palabras que sean groseras separadas por un espacio -> ')
            texto = input('Dame una frase la cual contenga una que otra palabra es la que no te gusta ploxs -> ')
            pal_camb = input('Dime la palabra por la cual quieres cambiar las palabras que no te gustan -> ')
            print(censura(palabras=pal, texto=texto, palabra_cambio=pal_camb))
        elif opc == 2:
            pal2 = input('Dame una lista de las palabras que sean groseras separadas por un espacio -> ')
            texto2 = input('Dame una frase la cual contenga una que otra palabra es la que no te gusta ploxs -> ')
            pal_camb2 = input('Dime la palabra por la cual quieres cambiar las palabras que no te gustan -> ')
            n = int(input('Dime la diferencia valida de caracteres entre las cedenas -> '))
            print(limite_censura(palabras=pal2, texto=texto2, palabra_cambio=pal_camb2, diferencia=n))
        elif opc == 3:
            print('Adios sujeto grosero')
            salir = True
        else:
            print('Elige una de las opciones... :D')


if __name__ == '__main__':
    main()
