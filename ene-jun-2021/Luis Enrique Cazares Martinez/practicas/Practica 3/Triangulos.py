def tipo_triangulo(a,b,c):
    if (a != 0 or b != 0 or c != 0) and ((a + c) > b and (a + b) > c and (b + c) > a):
        if a == b and b == c and a == c:
            return "Es un Triangulo Equilatero"
        elif (a == b and b != c):
            return "Es un Triangulo Isoceles"
        elif (a != b and a != c and b != c):
            return "Es un Triangulo Escaleno"
    else:
        return "No es un Triangulo"

if __name__ == "__main__":
    print("Introduce 3 valores para ver si son de un tringulo y de que tipo")
    a = input()
    b = input()
    c = input()
    print(tipo_triangulo(a,b,c))