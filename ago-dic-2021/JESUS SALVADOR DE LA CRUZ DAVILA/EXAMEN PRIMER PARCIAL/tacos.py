def lista_de_tacos(tacos):
    total = 0
    cachete = 0
    lengua = 0
    tripitas = 0
    pastor = 0
    machito = 0
    tamanio = 30

    precioCachete = 13
    precioLengua = 10
    precioTripitas = 9
    precioPastor = 15
    precioMachito = 14

    if tamanio <= 30:
        for t in tacos:
            if t == "cachete":
                cachete += 1
            if t == "lengua":
                lengua += 1
            if t == "tripitas":
                tripitas += 1
            if t == "pastor":
                pastor += 1
            if t == "machito":
                machito += 1
        total=  (cachete * precioCachete) + (lengua * precioLengua) + (tripitas * precioTripitas) + (pastor * precioPastor) + (machito * precioMachito)
        print(f'{cachete} cachete, {lengua} lengua, {tripitas} tripitas, {pastor} pastor, {machito} machito')

        print(f'El total es: {total}')
    else:
        print('Excediste el numero de tacos')

    return total

if __name__ == '__main__':
    tacos = list(map(str, input().split()))
    print(lista_de_tacos(tacos))


