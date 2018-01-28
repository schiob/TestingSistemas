def cuenta(pedido):
    cachete = pedido.count('cachete')
    tcachete= cachete * 13


    lengua = pedido.count('lengua')
    tlengua= lengua * 10


    tripitas = pedido.count('tripitas')
    ttripitas= tripitas * 9

    pastor = pedido.count('pastor')
    tpastor= pastor * 15


    machito = pedido.count('machito')
    tmachito= machito * 14


    suma = tcachete + tlengua + ttripitas + tpastor + tmachito

    
    return suma


if __name__ == "__main__":
    
    pedido = [] 
    tacos = input()
    pedido = tacos.split(' ')
    a = len(pedido)
    ok = cuenta(pedido)

    if 0 < a <= 30:
        print(ok)
    
    else:
        print("No puedes meter mas de 30 palabras....")



