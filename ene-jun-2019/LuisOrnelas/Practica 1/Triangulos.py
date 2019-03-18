a = float(input("Ingrese el Primer lado del Triangulo: "))
b = float(input("Ingrese el Segundo lado del Triangulo: "))
c = float(input("Ingrese el Tercer lado del Triangulo: "))

if (a+b)>c and (a+c)>b and (b+c)>a:
    print("\nLos lados corresponden a un Triangulo:")
    if (a==b==c):
        print("\tEquilatero")
    elif (a==b or a==c or b==c):
        print("\tIsosceles")
    else:
        print("\tEscaleno")
else:
    print("\nNo es un Triangulo")