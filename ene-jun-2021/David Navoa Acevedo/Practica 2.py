 # si los valores ingresados a, b, c entonces comparar y saber si es un triangulo equilatero escaleno etc. i si no lo es e imprimir el resultado
def tipo_triangulo(a , b , c ):

#equilatero Los 3 lados (a, b y c) son iguales          
  if a + b + c == 0:
    print("no es un triangulo")
  elif a == b and a == c:
    print ("es un triangulo equilatero")  

    #Escaleno si los 3 lados son distintos
  elif a != b and a != c:
    print("Es un triangulo escaleno")

  #Isoseles Tienen 2 lados iguales (a y b) y un lado ]#distinto (c)
  elif a==b and a!=c: 
    print ("Es un triangulo Isoseles")

    #Condicion para que sea un triangulo
    #Que la suma de dos de sus lados sea mayor que el otro
  elif (a + b) < c or (b + c) < a or (a + c) < b:
    print("No es un triangulo")
    
print(tipo_triangulo(7,7,7))
print(tipo_triangulo(7,7,9))
print(tipo_triangulo(7,8,9))
print(tipo_triangulo(0,0,0))
print(tipo_triangulo(-2,0,6))