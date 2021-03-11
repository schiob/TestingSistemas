
def total(pedido):

    precio = {"cachete": 13, "lengua": 10, "tripitas": 9, "pastor": 15, "machito": 14}
    costo_total = 0

    for taco in pedido:
        if taco in precio.keys():
            costo_total += precio[taco]

    return costo_total

pedido = list(input().split())

print(total(pedido))

if __name__ == '__main__':

    pedido = list(input().split())
    print(total(pedido))
