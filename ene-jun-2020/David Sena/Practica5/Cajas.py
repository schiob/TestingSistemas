import numpy
import math

def Volumen_Caja(lado1, lado2, lado3):
    volumen = lado1 * lado2 * lado3
    return volumen
 


def Contenido(content):
    cajas=[]
    litros=[]
    total=[]
    for i in range(0,3):
        caj=float(input("Numero de Contenedores:  "))
        lit=float(input("Numero de Litros: "))

        cajas.append(caj)
        litros.append(lit)      
        total.append(cajas[i]*litros[i])
    print(sum(total))

def Funcion_Principal(lado1,lado2,lado3,total):
    caja1 = Volumen_Caja(lado1,lado1,lado1)
    caja2 = Volumen_Caja(lado2,lado2,lado2)
    caja3 = Volumen_Caja(lado3,lado3,lado3)
    count = 0
    lista = []
    while total > caja1:
        total -=caja1
        count+=1
    if total < caja1:
        lista.append([count,caja1])
        count = 0
    while total > caja2:
        total -= caja2
        count += 1
    if total < caja2:
        lista.append([count,caja2])
        count=0
    while total > 0:
        total -= caja3
        count += 1
    lista.append([count,caja3])
    return lista


if __name__ == "__main__":
    total_volumen = Volumen_Caja(1,5,3)
    print(total_volumen)
    vol_contenido =((5,4),(2,3),(6,2))
    print(Contenido(vol_contenido))
    print(Funcion_Principal(4,3,2,100))
