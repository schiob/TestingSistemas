def volumen(long,anch,alt):
   if(type(long) == int and type(anch) == int and type(alt) == int):
     volumen = long*anch*alt
     return volumen
   else:
     return print("Un lado no es entero")     

def lista(lista):
    res=0
    b=0
    x=0
    for n in lista:
        n=0
        res+=(lista[b][x]*lista[b][x+1])
        b+=1
        n+=1
    return res

def calcularcajas(lado1,lado2,lado3,volumenF):
    mayor = max(lado1,lado2,lado3)
    menor = min(lado1,lado2,lado3)
    medio = lado1+lado2+lado3-menor-mayor

    volumena = 0
    nmayor=0
    nmedio=0
    nmenor=0
    while volumena <= volumenF:
        x=volumen(mayor,mayor,mayor)
        if (volumena+x > volumenF):
            break
        else:
            volumena+=volumen(mayor,mayor,mayor)
            nmayor+=1

    while volumena <= volumenF:
        x=volumen(medio,medio,medio)
        if (volumena+x > volumenF):
            break
        else:
            volumena+=volumen(medio,medio,medio)
            nmedio+=1

    while volumena < volumenF:
            volumena+=volumen(menor,menor,menor)
            nmenor+=1
    listasi =((nmayor,volumen(mayor,mayor,mayor)),(nmedio,volumen(medio,medio,medio)),(nmenor,volumen(menor,menor,menor)))
    return lista(listasi)

if __name__ == "__main__":
    res = volumen(1,1,.4)
    print(res)
    liston =((5,4),(2,3),(6,2))
    print(lista(liston))
    print(calcularcajas(4,3,2,100))



    
