def tri(val):
    nt = (val*(val+1))/2
    return nt

if __name__ == '__main__':

    n = int(input("Que poisicion deseas conocer? "))
    res = int(tri(n))
    print("El numero de la posicion {} es: {}".format(n,res))
