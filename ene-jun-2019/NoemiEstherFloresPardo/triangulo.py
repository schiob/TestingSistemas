a=float(input("Ingrese el primer lado del triángulo: "))
b=float(input("Ingrese el segundo lado del triángulo: "))
c=float(input("Ingrese el tercer lado del triángulo: "))

if(a+b)>c and (a+c)>b and (b+c)>a:
    print("Es un triángulo: ")

    if(a==b==c):
        print("Equilátero")
    elif(a==b or a==c or b==c):
        print("Isósceles")
    else:
        print("Escaleno")

else:
    print("No es un triángulo")