import unittest
def tacos(pedido):
    pedido = list(map(str,pedido.split()))
    cachete = 0
    lengua = 0
    tripitas = 0
    pastor = 0
    machito = 0
    tacos_cachete = 13
    tacos_lengua = 10
    tacos_tripitas = 9
    tacos_pastor = 15
    tacos_machito = 14

    if len(pedido) >= 30:
        return("Error")
    for i in range(len(pedido)):
        if pedido[i] == "cachete":
                cachete +=1
        elif pedido[i] == "lengua":
                lengua +=1
        elif pedido[i] == "tripitas":
                tripitas +=1
        elif pedido[i] == "pastor":
                pastor +=1
        elif pedido[i] == "machito":
                machito +=1
        else:
            continue
    
    cuenta = (cachete * tacos_cachete + lengua * tacos_lengua + tripitas * tacos_tripitas + pastor * tacos_pastor + machito * tacos_machito)
    print (cuenta)
    return cuenta

if __name__ == '__main__':
    pedido = input("Ingrese su pedido")
    tacos(pedido)