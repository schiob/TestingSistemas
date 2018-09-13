def Prueba3NTriangulo(n):
    formula = (n*(n+1))/2
    return n,formula
if __name__ == '__main__':
    entrada = int(input("¿Qué número triangular quieres conocer?: "))
    salida = Prueba3NTriangulo(entrada)
    print("<Posicion {}>,<Numero triangular {}>".format(salida[0], salida[1]))