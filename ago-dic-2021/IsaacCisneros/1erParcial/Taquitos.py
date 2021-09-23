def total(pedido):
    
    precio = {"cachete": 13, "lengua": 10, "tripitas": 9, "pastor": 15, "machito": 14, "bistek": 18}
    costo_total = 0
    if len(precio) > 30:
        return("maximo 30 tacos por orden")

    for taco in pedido:
        if taco in precio.keys():
            costo_total += precio[taco]

    return costo_total
print("¿De cuales quieres?")

if __name__ == '__main__':

    pedido = list(input().split())
    print(total(pedido))
    print("¿De cuales quieres?")