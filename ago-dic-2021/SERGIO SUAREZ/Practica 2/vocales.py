def count():
    txt = input('Escribe una frase: ')
    contador = 0
    for letter in txt:
        if letter in "aeiou":       
            contador += 1
    print('Total de vocales: ', contador)

count()