lados=input("Escribe los lados del triangulo:").split()
def triangulos(lados):
    if lados[0]+lados[1]>lados[2] or lados[1]+lados[2]>lados[0] or lados[2]+lados[0]>lados[1]:
        if lados[0].isalpha()==True or lados[1].isalpha()==True or lados[2].isalpha()==True :
            print("No se admiten letras.")
        elif lados[0]==lados[1] and lados[1]==lados[2]: 
            print("Es equilatero")
        elif int(lados[0])<=0 or int(lados[1])<=0 or int(lados[2])<=0:
            print("No puedes poner ceros o negativos.")
        elif lados[0]==lados[1] or lados[0]==lados[2] or lados[1]==lados[2]:
            print("Es isoceles")
        elif lados[0]!=lados[1] or lados[0]!=lados[2] or lados[1]!=lados[2]:
            print("Es escaleno")
        return
    else:
        print("No se puede contruír")
triangulos(lados)


triangulos(1,1,1)
triangulos(0,2,1)
triangulos(4,5,7)
triangulos(a,b,c)
triangulos(7,7,7)
