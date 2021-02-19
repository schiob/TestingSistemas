 # si los valores ingresados a, b, c entonces comparar y saber si es un triangulo equilatero escaleno etc. i si no lo es e imprimir el resultado
def tipo_triangulo(a , b , c ):

  #Checar que vengan los 3 datos
  if a is None or b is None or c is None:
    return "No es un Triangulo"
  #Condicional para saber si hay una letra
  if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
    return "No es un Triangulo"
#equilatero Los 3 lados (a, b y c) son iguales          
  if a <= 0 or b <= 0 or c <= 0:
    return "No es un Triangulo"
  if sum([a, b, c]) < max([a, b, c]):
    return "No es un Triangulo"
  #Equilatero es el que tiene los 3 lados iguales
  if a == b and a == c:
    return "Es un triangulo Equilatero"  
    #Escaleno si los 3 lados son distintos
  elif a != b and a != c:
    return "Es un triangulo Escaleno"
  #Isoseles Tienen 2 lados iguales (a y b) y un lado ]#distinto (c)
  if a == b and a != c: 
    return "Es un triangulo Isoseles"


    