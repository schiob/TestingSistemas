import operator

class pantalon:
  def __init__(self, Marca, Precio):
    self.Marca = Marca
    self.Precio = Precio

# #########

def vendePantalones(N,X,listap):
  listaDos=[]

  if(X>N):
   return 0
  
  listaDos=sorted(listap,key=operator.attrgetter("Precio"))
  validarTotal=0

  marcas = [p.Marca for p in listaDos]
  numMarcas = {i: marcas.count(i) for i in marcas}

  pantalonVendido=0
  p=N

  while p>X:

    if X<0:
      return 0

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

  return f"{pantalonVendido} {validarTotal}"
##########
listap = []
N, X = [int(i) for i in input("\nIngresa la cantidad inicial y final\n").split()]
  
for i in range(N):
  # print("ingresa la marca y precio")
  x , y = [int(i) if i.isdecimal() else str(i) for i in input().split()]
  listap.append(pantalon(x,y))


print(vendePantalones(N,X,listap))