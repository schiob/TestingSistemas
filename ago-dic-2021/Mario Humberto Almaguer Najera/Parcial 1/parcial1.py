def taquitos():
    print('-----MENU-----\nCachete\nLengua\nTripitas\nPastor\nMachito')
    entrada = input('Escriba su orden min: 0 max: 30 tacos separados por espacio: ').title()
    orden = list(entrada.split())

def total_pagar(orden : list):
    total = 0

    if (len(orden) <= 30):
        for taco in orden:
            if taco == 'Cachete':
                total += 13
            elif taco == 'Lengua':
                total += 10
            elif taco == 'Tripitas':
                total += 9
            elif taco == 'Pastor':
                total += 15
            elif taco == 'Machito':
                total += 14
            else:
                return 'El/Un taco no existe'
    else:
        return('Solo se aceptan 30 tacos como maximo.')

    return total


if __name__ == '__main__':
    orden = ['Cachete', 'Lengua', 'Tripitas', 'Pastor']
    totalPagar = total_pagar(orden)
    print('Total a pagar: ', totalPagar)
