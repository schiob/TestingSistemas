def contar_vocales():
    frase = input('Escribe tu frase: ')
    contador = 0
    for letra in frase:
        if letra in "aeiou":       
            contador += 1
    print('Vocales: ', contador)

contar_vocales()