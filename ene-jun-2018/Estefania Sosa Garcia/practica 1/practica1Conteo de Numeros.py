
import sys
sys.stdin
# cadena=sys.stdin.readline()
# cadena.split()
cadena = list(map(int, input().strip().split(' ')))

neg=0
pos=0
par=0
imp=0
for i in cadena:
       if (i<0):
               neg+=1
       if (i>0):
               pos+=1
       if ((i%2)==0):
               par+=1
       if ((i%2)!=0):
               imp+=1
 	

print('''
son {} pares
son {} negativos
son {} positivos
son {} impares

	'''.format(par,neg,pos,imp))


