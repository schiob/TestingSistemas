#Practica 2
import random
import numpy as np
Test_Cases=open("P2_Test_Cases.txt","r")#Es el archivo con los casos de prueba
#Lectura de los casos de prueba y organización en listas
Lines=Test_Cases.readlines()
cases=[]
res=[]
for i in Lines:
    line=i.split(' ')
    cases.append(line[0:2])
    res.append(int(line[2]))
#Convierte los elementos string en int
cases=[[int(i) for i in j] for j in cases]
    
#método
def suma(a, b):
    #Descomentar para ver los números y los resultados
    #print(a)
    #print(b)
    #print(a+b)
    #print("------")
    return a+b

#método test
def test_answer(x,y,r):
    assert suma(x,y)==r

for i in range(len(cases)):
    test_answer(cases[i][0], cases[i][1], res[i])