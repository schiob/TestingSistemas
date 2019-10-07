
#metodo
def cuenta(pedido):
    
    cachete = pedido.count('cachete')
    lengua = pedido.count('lengua')
    tripas = pedido.count('tripas')
    pastor = pedido.count('pastor')
    machito = pedido.count('machito')

    suma = cachete*13 + lengua*10 + tripas*9 + pastor*15 + machito*14
    return suma
#metodo
print ("Dame tu pedido")
if __name__ == "__main__":
    
    pedido = []
    tacos = input()
    pedido = tacos.split(' ')
    x = len(pedido)
    
 #ciclo   
    if 0 < x <= 30:
       print(cuenta(pedido))
    else:
        print("No puedes pedir mas de 30 palabras....")
