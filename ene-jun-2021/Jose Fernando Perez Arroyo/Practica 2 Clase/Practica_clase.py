def trian(a, b, c):
        if a==b and a==c:
            return 'Equilatero'
        if a != b and a != c:
            return 'Escaleno'
        else:
            return 'Isoceles'
     
n=0
while n == 0 :
    print('Deseas hacer una prueba de los lados(Elige Y o N):')
    x=input()
       
    if x == 'Y' or x == 'y':
        print('Dame el lado 1: ')
        a = int(input())
        print('Dame el lado 2: ')
        b = int(input())
        print('Dame el lado 3: ')
        c = int(input())
        print(trian(a,b,c))     
    elif x =='N' or x=='n':
        break
    else:
       print('Error Termino no valido')

