import math
def volumenCilindro():
    while(True):
        flag=False
        try:
            r=float(input("Por favor ingrese radio del cilindro"))
            h=float(input("Por favor ingrese altura del cilindro"))
        except:
            flag=True
        if flag==True:
            print("Ocurrio un error, Reintentalo por favor")
        else:
           break
    v = r * h * math.pi
    return v

print(volumenCilindro())          