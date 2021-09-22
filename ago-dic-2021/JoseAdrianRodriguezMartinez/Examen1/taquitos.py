
def crear_lista(pedido: str):
    lista = list(pedido.split(' '))
    return lista

def total_pedido(pedido: list):
    total_parcial = 0
    cachete = 13
    lengua = 10
    tripitas = 9
    pastor = 15
    machito = 14
    for i in pedido:
        if i == 'cachete':
            total_parcial+= cachete
        elif i == 'lengua':
            total_parcial+= lengua
        elif i == 'tripitas':
            total_parcial+= tripitas
        elif i == 'pastor':
            total_parcial+= pastor
        elif i == 'machito':
            total_parcial+= machito
    return total_parcial

if __name__ == '__main__':
    lista = crear_lista(input('Pedido separado por espacios: '))
    total = total_pedido(lista)
    print(total)