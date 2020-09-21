from operator import itemgetter

# ME GUSTAN LOS GATOS ... !!!

# ENTRADAS:
# N -> Número de pantalones.
# X -> Pantalones a los que se desea llegar.

# REGLAS:
# Mantener por lo menos 1 pantalon de cada marca.
# Pantalones más caros se les darán prioridad.
# Vender máximo 5 pantalones de cada marca.

# Imprime los valores de la lista de pantalones (uso exclusivo para pruebas).
def printPants(pants):
  for it in pants:
    print(str(it))

# Obtenemos los datos que utilizará el programa.
def getData():
  pants = []

  # obtenemos el número de pantalones y el número de pantalones a vender
  N, X = input().split(" ")
  
  # convertimos los valores a enteros
  N = int(N)
  X = int(X)

  # los almacenamos en una lista de diccionarios, tal que cada diccionario representa un pantalon
  for i in range(N):
    ptype, price = input().split(" ")
    pants.append({
      "ptype": ptype,
      "price": float(price)
    })

  # devolvemos los datos en un diccionario
  return {
    "N": N,
    "X": X,
    "pants": pants
  }

# Ordena los pantalones por marca y luego por precio de forma ascendente.
def sortPants(pants):
  return sorted(
    pants,
    key = itemgetter("ptype", "price"),
    reverse = True
  )

# Obtiene una lista de los pantalones que pueden ser vendidos, tomando en cuenta:
# - No pueden venderse más de 5 pantalones por marca.
# - Debe de mantenerse por lo menos 1 pantalon por marca.
# - Se deben de vender los más caros.
def getCandidates(pants):
  if not len(pants):
    return []
  
  lastType = pants[0]["ptype"]
  candidates = []
  nCandidatesByType = 0
  
  for p in pants:
    # Si la marca del pantalón actual es diferente al anterior, significa que fue añadido a la lista el último pantalón de una marca posible, entonces lo eliminamos de la lista para que mantenga por lo menos un pantalón posible de esa marca...

    # ooooooooooo...

    # Sobrepaso el número máximo de pantalones para vender de la marca actual...
    if p["ptype"] != lastType or nCandidatesByType > 5:
      candidates.pop()
      nCandidatesByType = 0

    # Añadimos el pantalon a la lista de los pantalones a vender
    candidates.append(p)

    # registramos el nombre de la marca del pantalon actual para su uso en la siguiente iteración
    lastType = p["ptype"]
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
    key = lambda c: c["price"],
    reverse = True
  )

  # vendemos y contamos las ganancias
  money = 0
  for i in range(count):
    money += candidates[i]["price"]

  return money

if __name__ == "__main__":
  # === PASOS DEL ALGORITMO ===
  # 1 .- Obtiene los datos del input
  myData = getData()

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