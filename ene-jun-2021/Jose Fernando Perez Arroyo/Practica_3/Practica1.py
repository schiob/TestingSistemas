def pruebarara(c):   #cadena= input("Dame una lista de numeros: ").split(" ")'# d=list(cadena)#tam=len(cadena)#d= list(map(int, d))#print(d)
    va=c.split(" ")
    for i in range(len(va)):
        try:  
            for q in range(len(va)):
                va[q] = int(va[q])
            a= va[i]
            b=  int(va[i])
            if a == b:
                cpo = cne = cim = cpar=0
                for x in range(len(va)):
                    if va[x]==0:
                        cpar+=1
                    else:
                        if va[x]>=0:
                            cpo+=1
                            if va[x] % 2==0:
                                cpar=cpar+1
                            else:
                                cim=cim+1
                        else:
                            cne+=1
                            if va[x] % 2==0:
                                cpar=cpar+1
                            else:
                                cim=cim+1
                fqa = cpo, "número(s) positivo(s)\n", cne," número(s) negativos(s)\n", cpar," número(s) par(es)\n", cim," número(s) impar(es)"
                return fqa
        except:
            return 'Error digitaste una letra'

if __name__ == "__main__":
    pruebarara(c)
