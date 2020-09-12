class pantalon:
  def __init__(self, Marca, Precio):
    self.Marca = Marca
    self.Precio = Precio



import operator

listap = []
listaDos=[]
print("ingresa la cantidad inicial y final")
N, X = input().split()
N=int(N)
X=int(X)

if(X>N):
  print(0)
  exit()

for i in range(N):
 print("ingresa la marca y precio")
 x , y = input().split()
 x = str(x)
 y = int(y)
 listap.append(pantalon(x,y))

listaDos=sorted(listap,key=operator.attrgetter("Precio"))

validarTotal=0

marcas = [p.Marca for p in listaDos]
numMarcas = {i: marcas.count(i) for i in marcas}

pantalonVendido=0
p=N

while p>X:
  if X<0:
    print(0)
    exit()


  objeto=listaDos[p-1]
  repetido=sum(objeto.Marca==l.Marca for l in listaDos )

  validaCincos=numMarcas[objeto.Marca] 

  if validaCincos-repetido>=5: 
    p-=1
    X-=1
    continue

  if repetido >1:
    validarTotal += listaDos[p-1].Precio 
    listaDos.remove(objeto)
    pantalonVendido+=1
    p-=1
  else:
    p-=1
    X-=1
    continue




print(pantalonVendido, validarTotal)