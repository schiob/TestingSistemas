import math


def volum(lado):
    vol = lado ** 3
    return vol


def contLiq(contenido):
    caja = []
    liquido = []
    total = []
    for arg in range(0, 3):
        box = int(input('Número de cajas: '))
        liq = int(input('Cantidad de Liquido: '))

        caja.append(box)
        liquido.append(liq)
        total.append((caja[arg] * liquido[arg]))
    print(sum(total))


def Total(lado, total):
    caja1 = volum(lado)
    caja2 = volum(lado)

    i = 0
    final = []
    while total > caja1:
        total -= caja1
        i += 1
    if total < caja1:
        final.append([i, caja1])
        i = 0
    while total > caja2:
        total -= caja2
        i += 1
    if total < caja2:
        final.append([i, caja2])
    return final


if __name__ == "__main__":

    print('Volumen Caja: ' + str(volum(3)))
    liquido = ((5, 4), (2, 3), (6, 2))
    print(contLiq(liquido))
    print(Total(3, 100))
