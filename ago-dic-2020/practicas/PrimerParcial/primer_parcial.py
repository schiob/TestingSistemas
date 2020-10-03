
file=open("/ago-dic-2020/practicas/PrimerParcial/triangulo.txt", "r")
print(file.read())

def tipo(a, b, c):
     if a==b and a==c:
         return 'Equilatero'
     elif a!=b and a!=c:
         return 'Escaleno'
     elif a==0 or b==0 or c==0:
         return 'No es triangulo'
     else:
         return 'Isóceles'

print(tipo(1, 1, 1))