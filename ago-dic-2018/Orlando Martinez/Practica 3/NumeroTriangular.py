def calcular(Numeros):
        resultado=(Numeros*(Numeros+1)/2)
        return resultado

if __name__ == '__main__':
    Numeros=int(input("Ingrese numero: "))
    resultado=calcular(Numeros)
    print("Numero {} : resultado {}".format(Numeros,resultado))
