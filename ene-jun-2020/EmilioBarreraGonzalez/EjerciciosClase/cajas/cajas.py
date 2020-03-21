import math as m
def volumen(lado1,lado2,lado3): ##Lo obtenido son m^3
    return float(lado1*lado2*lado3)

def cont(lista:list): ##Lo obtenido son litros
    total=0
    e=0
    for i in lista:
        x=i.split(",")
        e+=1
        total+=float(x[0])*float(x[1])
    return total

def transformacion(lista:list, lado1,lado2,lado3):
    vol=volumen(lado1,lado2,lado3) * 1000
    content=cont(lista)
    return m.ceil(content/vol)

if __name__=="__main__":
    lado1=4
    lado2=4
    lado3=4
    lista=["3,8","4,9","3,.5"]
    print(volumen(lado1,lado2,lado3))
    print(cont(lista))
    print(transformacion(lista,lado1,lado2,lado3))