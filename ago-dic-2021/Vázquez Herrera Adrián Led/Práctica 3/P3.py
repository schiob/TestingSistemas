#Práctica 3

def NumerosJuanita(e):
    #Contadores: Positivo, Negativo, Par, Impar
    cpo=cn=cpa=ci=0
    for i in range(len(e)):
        if e[i]>0: cpo+=1
        elif e[i]!=0: cn+=1
        if e[i]%2>0: ci+=1
        else: cpa+=1

    r=str(cpo)+" numero(s) positivo(s)\n"+str(cn)+" numero(s) negativo(s)\n"
    r+=str(cpa)+" numero(s) par(es)\n"+str(ci)+" numero(s) impar(es)\n"
    return (r)


