from typing import cast
def cuenta(pedido):
    lista_taco = pedido.split()
    menu = ['cachete', 'lengua', 'tripitas', 'pastor', 'machito']
    costo = [13,10,9,15,14]
    cuenta_total = 0
    if (len(lista_taco) > 30 or len(lista_taco) < 1):
        return 'Por favor, ingrese un pedido mayor a 0 y menor a 30.'
    else:
        for t in lista_taco:
            if t == menu[0]:
                cuenta_total += costo[0]
            elif t == menu[1]:
                cuenta_total += costo[1]
            elif t == menu[2]:
                cuenta_total += costo[2]
            elif t == menu[3]:
                cuenta_total += costo[3]
            elif t == menu[4]:
                cuenta_total += costo[4]
    return (f'Total a pagar: {cuenta_total}')

if __name__ == "__main__":
    l = "cachete lengua cachete tripitas machito machito machito cachete lengua"
    print(cuenta(l))


