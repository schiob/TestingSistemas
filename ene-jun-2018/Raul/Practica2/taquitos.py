pedido = [] 
tacos = input()
pedido = tacos.split(' ')

a = len(pedido)

if a <= 30:
    
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

    print("Suma: " , suma )

else:
    print("No puedes meter mas de 30 palabras....")
