#TesteoP3
from P3 import *
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

#método test
def test_answer(x,r):
    assert NumerosJuanita(x)==r
    
for j in range(len(cases)):
    print(j)
    test_answer(cases[j],res[j])