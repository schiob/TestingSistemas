

class volumen:

    def calVol(l,a,h):
        largo = l
        ancho = a
        alto = h
        vol = 0

        vol = largo*ancho*alto
    
        return vol


if __name__ == "__main__":
    
    l = int(input("Escriba el largo:"))
    a = int(input("Escriba el ancho:"))
    h = int(input("Escriba la altura:"))

    print("-----Mostrando Resultado-----")
    print(volumen.calVol(l,a,h))
    




