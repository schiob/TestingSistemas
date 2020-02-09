class ChessxD:

    def __init__(self, x = 0, y = 0, dist = 0): ##funcion que recibira la posicion del caballo 
        self.x = x 
        self.y = y 
        self.dist = dist

    def estaDentro(x, y, n): ## Vamos a verificar que no se vaya a salir del tamano del tablero
    if (x >= 1 and x <= n and y >= 1 and y <= n):  
        return True
    return False

    def Movimientos(posCaballo,posObjetivo,TamañoT):

        ##Movimientos posibles que puede realizar el Caballo
        dx = [-2,-2,-1,1,2,2,1,-1]
        dy = [1,-1,2,2,1,-1,-2,-2]


#valores de entrada en el tablero

if __name__ == "__main__":

    n = 64
    Cabpos = []
    Cabpos.append(input("Posición en X: "))
    Cabpos.append(input("Posición en Y: "))

    