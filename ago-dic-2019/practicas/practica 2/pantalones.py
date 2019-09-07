class Item():
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio
    def __repr__(self):
        return "Marca: {0}  Precio: {1}".format(self.marca, self.precio)

class Pair():
    def __init__(self, pair1, pair2):
        self.limit = pair1
        self.exist = pair2
    def __repr__(self):
        return "Limit: {0}  Exist: {1}".format(self.limit, self.exist)

    def CanSell(self):
        if self.limit < 6 and self.exist > 1:
            return True
        return False

#Entrada
n, x = map(int, input().split())

lista = []
mapa = {}
for _ in range(n):
    marca, precio = input().split()
    lista.append(Item(marca, int(precio)))

    if marca in mapa:
        mapa[marca].exist += 1
    else:
        mapa[marca] = Pair(0, 1)

total = 0
items_cant = 0

for item in reversed(sorted(lista, key=lambda x: x.precio)):
    marca = item.marca
    if (n - items_cant) <= x:
        break
    if mapa[marca].CanSell():
        total += item.precio
        items_cant += 1
        mapa[marca].limit += 1
        mapa[marca].exist -= 1

if (n - items_cant) <= x:
    print(items_cant, total)

else:
    print(0)
