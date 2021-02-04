#a,b,c,d,e = input().split()

def trian(a, b, c):
    if a==b and a==c:
        return 'Equilatero'
    if a != b and a != c:
        return 'Escaleno'
    else:
        return 'Isoceles'
 
print('Dame numero de triangulos ')
n = int(input())

for i in range (n):
  print('Dame el lado 1: ')
  a = int(input())
  print('Dame el lado 2: ')
  b = int(input())
  print('Dame el lado 3: ')
  c = int(input())
  print(trian(a,b,c))