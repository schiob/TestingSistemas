print("Ingrese el primer numero")
lado1= input()
print("Ingrese el segundo numero")
lado2=input()
print("Ingrese el tercer numero")
lado3=input()

if (lado1+lado2)>lado3 and (lado1+lado3)>lado2 and (lado2+lado3)>lado1:
    print("Si es un triangulo")
    if(lado1==lado2==lado3):
        print("Equilatero")
    elif(lado1==lado2 or lado2==lado3 or lado1==lado3):
            print("Isoceles")
    else: print ("Isoceles")
else:
    print("No es triangulo")