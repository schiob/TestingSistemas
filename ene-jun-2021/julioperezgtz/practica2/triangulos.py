l=input("Lados del triangulo:").split()
def triangulos(l):
    if l[0].isalpha()==True or l[1].isalpha()==True or l[2].isalpha()==True:
        print("No se admiten letras.")
    elif l[0]==l[1] and l[1]==l[2]: 
        print("Es equilatero")
    elif int(l[0])<=0 or int(l[1])<=0 or int(l[2])<=0:
        print("No puedes poner ceros o negativos.")
    elif l[0]==l[1] or l[0]==l[2] or l[1]==l[2]:
        print("Es isoceles.")
    elif l[0]!=l[1] or l[0]!=l[2] or l[1]!=l[2]:
        print("Es escaleno.")
    return
triangulos(l)