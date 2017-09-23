# Lee los lados de una figura y determina si es un triángulo o no y de que tipo.

def tri_from_file(path):
    with open(path, 'r') as f:
        # Leer archivo y almacenar en una lista.
        side = f.read().split()

        # Test tres lados.
        if len(side) != 3:
            # Si hay más o menos de tres lados no es un triángulo.
            result = 'No triángulo.'
            return result

        # Test numérico.
        for x in side:
            # Si encuentra un caractér no numérico se determina que no es un triángulo.
            if x.isnumeric() == False:
                result = 'No triángulo.'
                return result

        # Los elementos de la lista se convierten a entero.
        side = list(map(int, side))

    # Test de cero y negativos.
    for x in side:
        # Si encuentra un cero o negativo se determina que no es un triángulo.
        if x < 1:
            result = 'No triángulo.'
            return result

    # Test de desigualdad triangular.
    inequality_flag = False
    if side[0] + side[1] > side[2] and side[1] + side[2] > side[0] and side[0] + side[2] > side[1]:
        inequality_flag = True

    # Si no pasa el test o está recibiendo más de 3 lados del archivo:
    # -> No es un triángulo.
    if inequality_flag == False:
        result = 'No triángulo.'
    else:
        # Si hay 3 números iguales en la lista, es equilatero.
        if len(set(side)) == 1:
            result = 'Equilátero.'
        # Si hay 2 números iguales en la lista, es isóceles.
        elif len(set(side)) == 2:
            result = 'Isóceles.'
        # Si ninguna de las anteriores se cumple, es escaleno.
        else:
            result = 'Escaleno.'

    return result

if __name__ == '__main__':
    print(tri_from_file("sides.txt"))
