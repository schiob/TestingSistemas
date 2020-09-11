import sys


sys.stdout.write("Escribe los numeros a sumar")
sys.stdout.flush()
n=sys.stdin.readline()
m=list(map(float,n.split()))
if len(m) > 2:
    print('inserta solo dos numeros')
else:
    print(sum(m))



class pantalon:
  def __init__(self, Marca, Precio):
    self.Marca = Marca
    self.Precio = Precio



import operator
listap = []
listaDos=[]
N, X = input().split()
N=int(N)
X=int(X)
vendidos=0
for i in range(N):
 x , y = input().split()
 x = str(x)
 y = int(y)
 listap.append(pantalon(x,y))

listaDos=sorted(listap,key=operator.attrgetter("Precio"))

def contarRepetidos(lisp,objp):
  cuenta=0
  for t in lisp:
    if objp in lisp:
      cuenta+1

  return cuenta

for i in listaDos:
  totaldisponibles=0
totaldisponibles = contarRepetidos(listaDos,i)
if totaldisponibles >1:

  print(i.Marca,i.Precio)


