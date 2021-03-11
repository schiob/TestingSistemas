
def tipo_de_triangulo(a,b,c):

    if None in [a,b,c]:
        return "No triangulo"

    if isinstance([a,b,c], str):
        return "No triangulo"

    if a <= 0 or b <=0 or c <= 0:
        return "No triangulo"
    
    if (sum([a,b,c]))-max([a,b,c]) <= max([a,b,c]):
        return "No triangulo"
    
    if a==b and b==c:
        return "Equilatero"
    elif a==b or b == c or a == c:
        return "Isosceles"
    
    return "Escaleno"

    

if __name__ == "__main__":    

    print('Dame numero de triangulos ')
    n = int(input())

    for i in range (n):
        print('Dame el lado 1: ')
        a = int(input())
        print('Dame el lado 2: ')
        b = int(input())
        print('Dame el lado 3: ')
        c = int(input())
        print(tipo_de_triangulo(a,b,c))