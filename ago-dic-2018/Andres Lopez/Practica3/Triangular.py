def triangular(n):
    T = (n*(n+1))/2
    return T
if __name__ == '__main__':
    n = int(input("Cual es tu numero Triangular "))
    res = triangular(n)
    print("El numero de la posicion {} es: {}".format(n,res))
