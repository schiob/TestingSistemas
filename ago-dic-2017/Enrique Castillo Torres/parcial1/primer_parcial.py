
def tri(path):
    with open("pre.txt", "r") as f:
        f = open(path)
        enteros = list(map(int, f.read().strip().split(' ')))
        a = enteros[0]
        b = enteros[1]
        c = enteros[2]

    if (a + b) > c and (a + c) > b and (b + c) > a:

        if (a == b == c):
            return 'Equilatero'

        elif (a == b or a == c or b == c):
            return 'Isosceles'

        else:
            return 'Escaleno'

    else:
        return 'No es triangulo'
    f.close()

if __name__ == '__main__':
    print(tri("pre.txt"))
