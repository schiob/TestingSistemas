#Testeo Parcial_1
from Parcial_1 import*

Test_Cases=open("Par1_Test_Cases.txt","r")#Es el archivo con los casos de prueba

#Lectura de los casos de prueba y organización en listas
Lines=Test_Cases.readlines()
cases=[]
res=[]
i=0
while i<len(Lines):
    cases.append(Lines[i])
    res.append(int(Lines[i+1]))
    i+=2

#método test
def test_answer(x,r):
    assert taquitos(x)==r
    
for j in range(len(cases)):
    print(j)#Casos que va probando
    test_answer(cases[j],res[j])
