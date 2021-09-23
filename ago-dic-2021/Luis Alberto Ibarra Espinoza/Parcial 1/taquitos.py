def taqueria(pedido):
    menu = {'cachete': 13, 'lengua': 10, 'tripita': 9, 'pastor': 15, 'manchito': 14}
    total = 0

    if (0 < (int(len((pedido)))) <= 30):
        for i in range(len(pedido)):
            taco = pedido[i]
            total += menu[taco]
        print(total)
    else:
        print('Se tienen que ordenar por lo menos 1 taco y maximo 30')

if __name__ == '__main__':
    orden = input().split()
    print(taqueria(orden))
