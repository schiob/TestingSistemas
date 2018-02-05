

def TipoTriangulo(a,b,c):
        ap = a + 1
        bp = b + 1
        am = a - 1
        bm = b - 1
    
        if a == b == c:
            if a == 0 and b == 0 and c == 0:
                print('No es triangulo')
            else:
                print('equilatero')

        if a == 0 and b == 0 and c != 0 or a == 0 and b != 0 and c == 0 or a != 0 and b == 0 and c == 0:
            print('No es triangulo')


        if a != b != c != a:
            if ap == b and bp == c and c == c or am == b and bm == c and c ==c:
                print('No es triangulo')
            else:
                print('escaleno')
        
        if a == b != c or a != b == c or a == c != b:
            if a == 0 and b == 0 and c != 0 or  a == 0 and b != 0 and c == 0 or a != 0 and b == 0 and c == 0:
                print("No es trinagulo")
            else:
                print('isoceles')

        return ''    


if __name__== "__main__":

    a1,b1,c1 =input().split(' ')
    a=int(str(a1))
    b=int(str(b1))
    c=int(str(c1))
    

    if -100 <= a <= 100 and -100 <= b <= 100 and -100 <= c <= 100:
        print(TipoTriangulo(a,b,c))
    else:
        print("No puedes teclear numeros mayores o igual a -100 y menos o igual a 100")

        


