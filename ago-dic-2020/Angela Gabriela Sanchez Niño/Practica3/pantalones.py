from operator import itemgetter


# ENTRADAS:
# N -> Número de pantalones.
# X -> Pantalones a los que se desea llegar.

# REGLAS:
# Mantener por lo menos 1 pantalon de cada marca.
# Pantalones más caros se les darán prioridad.
# Vender máximo 5 pantalones de cada marca.

jeans = 8 #ingrese numero de pantalones
venta = 5  #ingrese numero de pantalones a vender
pantalones = [{'marca': 'Patito', 'precio': 4},
        {'marca': 'Patito', 'precio': 5},
        {'marca': 'Levice', 'precio': 15},
        {'marca': 'Patito', 'precio': 5},
        {'marca': 'Levice', 'precio': 3},
        {'marca': 'Nike', 'precio': 20},
        {'marca': 'Nike', 'precio': 18},
        {'marca': 'Levice', 'precio': 4}]



def pantalones(pantalones): #funcion para imprimir lista de pantalones
  for i in pantalones:
    print(str(i))


def getdatos(p, m, pantalones): 
  
  # convertimos los valores a enteros
  pant= int(pant)
  m = int(m)

  
  return {
    "pant": pant,
    "m": m,
    "pantalones": pantalones
  }

def Ordenar(pantalones):
  return sorted(
    pantaloness,
    key = itemgetter("marca", "precio"),
    reverse = True
  )

# Obtiene una lista de los pantalones que pueden ser vendidos, tomando en cuenta:
# - No pueden venderse más de 5 pantalones por marca.
# - Debe de mantenerse por lo menos 1 pantalon por marca.
# - Se deben de vender los más caros.
def getCandidates(pantalones):
  if not len(pantalones):
    return []
  
  lastType = pants[0]["marca"]
  candidates = []
  nCandidatesByType = 0
  
  for p in pantaloness:
    # Si la marca del pantalón actual es diferente al anterior, significa que fue añadido a la lista el último pantalón de una marca posible, entonces lo eliminamos de la lista para que mantenga por lo menos un pantalón posible de esa marca...

    # ooooooooooo...

    # Sobrepaso el número máximo de pantalones para vender de la marca actual...
    if p["marca"] != lastType or nCandidatesByType > 5:
      candidates.pop()
      nCandidatesByType = 0

    # Añadimos el pantalon a la lista de los pantalones a vender
    candidates.append(p)

    # registramos el nombre de la marca del pantalon actual para su uso en la siguiente iteración
    lastType = p["marca"]
    nCandidatesByType += 1

  candidates.pop()
  return candidates

# Tratamos de vender los pantalones de la lista de los candidatos.
def tryToSell(count, candidates):
  # si no cumple con la cantidad mínima, no se venderá ninguno
  if len(candidates) < count:
    return 0
  
  # ordenamos por precio la lista de candidatos de forma descendente, para vender los primeros (los más caros)
  candidates = sorted(
    candidates,
    key = lambda c: c["precio"],
    reverse = True
  )

  #printPants(candidates)

  # vendemos y contamos las ganancias
  money = 0
  for i in range(count):
    money += candidates[i]["precio"]

  return money

# === PASOS DEL ALGORITMO ===
# 1 .- Obtiene los datos del input
myData = getData(numpants,numpantsvender,pants)

# 2 .- Ordena los datos por marca y precio de forma descendente
myData["pants"] = sortPants(myData["pants"])

# 3 .- Devuelve los pantalones que SÍ pueden venderse
candidates = getCandidates(myData["pants"])

# 4 .- Devuelve la ganancia obtenida
cSolds = myData["N"] - myData["X"]
money = tryToSell(cSolds, candidates)


# 5 .- Imprime el resultado final
if money > 0:
  print(f"{cSolds} {money}")
else:
  print("0")