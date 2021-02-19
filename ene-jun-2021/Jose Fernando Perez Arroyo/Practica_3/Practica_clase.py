def trian(a,b,c):
        if a.isalpha() == True or b.isalpha() == True or c.isalpha()==True:
            return 'digito un letra'
        elif a == b and a == c:
            return 'Equilatero'
        elif a == b or a == c or b == c:
            return 'Isoceles'
        elif int(a) <= 0 or int(b) <= 0 or int(c) <= 0:
            print('Lado negativo!!!!')
        elif int(a)!=int(b) or  int(a)!=int(c) or int(b) != int(c):
            return 'Escaleno'
        else:
            return 'No triangulo'

'if __name__ == "__main__":
 '   while n == 0 : 
        'print('Deseas hacer una prueba de los lados(Elige Y o N):')
        'x=input() 
        'if x == 'Y' or x == 'y':
         '   print('Dame el lado 1: ')
            'a = input()
            'print('Dame el lado 2: ')
            'b = input()
            'print('Dame el lado 3: ')
            'c = input()
            'print(trian(a,b,c))     
        'elif x =='N' or x=='n':
            'break
        'else:
        'print('Error Termino no valido')

