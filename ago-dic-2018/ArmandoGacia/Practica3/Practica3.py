def Triangulares(pos):
    num = (pos*(pos+1))/2
    #Este metodo devuelce la posicion y el numero triangular de esa posicion 
    return pos,num


if __name__ == '__main__':
    posicion = int(input("¿Cual numero triangular deseas conocer?"))
    salida = Triangulares(posicion)
    print("Numeros Triangulares")
    print("(Posicion,NumeroTringular)")
    print("({},{})".format(salida[0],salida[1]))
