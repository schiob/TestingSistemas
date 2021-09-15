#Práctica 3
#Nota de los casos de prueba: se debe poner un enter en la última fila
Test_Cases=open("P3_Test_Cases.txt","r")#Es el archivo con los casos de prueba
#Lectura de los casos de prueba y organización en listas
Lines=Test_Cases.readlines()
cases=[]
res=[]
i=0
while i<len(Lines)-2:
    line=Lines[i].split(', ')
    cases.append(line)
    reli=Lines[i+1]+Lines[i+2]+Lines[i+3]+Lines[i+4]
    res.append(reli)
    i+=5
    
#Convierte los elementos string en int
cases=[[int(k) for k in j] for j in cases]

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

#método test
def test_answer(x,r):
    assert NumerosJuanita(x)==r
    
for j in range(len(cases)):
    print(j)
    test_answer(cases[j],res[j])
