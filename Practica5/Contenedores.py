import math
def volumen(lado):
    vol = lado ** 3
    return vol

def contLiquido(contenido):
    caja = []
    liquido = []
    total = []
    for arg in range(0, 3):
        box = int(input('Contenedores:'))
        liq = int(input('Liquido total: '))
        
        caja.append(box)
        liquido.append(liq)
        total.append((caja[arg]*liquido[arg]))
    print(sum(total))

def Total(lado, total):
    box1 = volumen(lado)
    box2 = volumen(lado)

    i = 0
    final = []
    while total > box1:
        total -= box1
        i += 1
    if total < box1:
        final.append([i, box1])
        i = 0
    while total > box2:
        total -= box2
        i += 1
    if total <box2:
        final.append([i, box2])
    return final


if __name__ == "__main__":

    print('Volumen Caja: ' + str(volumen(3)))
    liquido = ((5,4),(2,3),(6,2))
    print(contLiquido(liquido))
    print(Total(3, 100))


