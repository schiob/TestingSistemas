def orden(tacosSplit):

    total = 0

    tacosTroceados = tacosSplit.split()

    if len(tacosTroceados) > 30:
        return('Hasta un maximo de 30 tacos por orden')
    elif len(tacosTroceados) == 0:
        return('Minimo un taco por orden')
    else:
        for taco in tacosTroceados:
            if taco == 'cachete':
                total = total + 13
            elif taco == 'lengua':
                total = total + 10
            elif taco == 'tripitas':
                total = total + 9
            elif taco == 'pastor':
                total = total + 15
            elif taco == 'machito':
                total = total + 14
            else:
                print(f'De {taco} no tengo joven')
                total = total

        return(f'Van a ser: ${total} mas propina joven')


if __name__ == '__main__':
    ordenTaquitos = input('¿De que va a querer joven?')
    print(orden(ordenTaquitos))
