def calcular_mov(cab, peones):
    if cab[0] in "ah": 
        if cab[1] in "18":
            return 2
        elif cab[1] in "27":
            return 3
        return 4
    if cab[0] in "bg":
        if cab[1] in "18":
            return 3
        if cab[1] in "27":
            return 4
        return 6
    if cab[1] in "3456" and cab[0] in "cdef":
        return 8
    if cab[1] in "18": 
        if cab[0] in "ah":
            return 2
        elif cab[0] in "bg":
            return 3
        return 4
    if cab[1] in "27":
        if cab[0] in "ah":
            return 3
        if cab[0] in "bg":
            return 4
        return 6
    return 8

def position(pos):
    for i in range(len(board)):
        
        for j in range(len(board[i])):
            if cab_pos == board[i][j]:
                #print(board[i][j])
                return board[i][j]
            

if __name__ == "__main__":
    #calcular_mov()

    #x = input("Escribe la posicion en x: ")
    #y = input("Escribe la posicion en y: ")
    ##La idea es dar la posicion del caballo y a partir de esto
    ##sumar posiciones en las listas 
    ## y regresar las posiciones donde los peones podrian comer al caballo
    ##Aun falta desarrollo
    cab_pos = input("Escribe la posicion del Caballo :")
    
    board = [['a1','b1','c1','d1','e1','f1','g1','h1'],
            ['a2','b2','c2','d2','e2','f2','g2','h2'],
            ['a3','b3','c3','d3','e3','f3','g3','h3'],
            ['a4','b4','c4','d4','e4','f4','g4','h4'],
            ['a5','b5','c5','d5','e5','f5','g5','h5'],
            ['a6','b6','c6','d6','e6','f6','g6','h6'],
            ['a7','b7','c7','d7','e7','f7','g7','h7'],
            ['a8','b8','c8','d8','e8','f8','g8','h8']]

    print(position(cab_pos))
            


    #mat = ['1a','1b','1c','1d','1e','1f','1g','1h', ##Posiciones del 0 a la 63
    #'2a','2b','2c','2d','2e','2f','2g','2h',
    #'3a','3b','3c','3d','3e','3f','3g','3h',
    #'4a','4b','4c','4d','4e','4f','4g','4h',
    #'5a','5b','5c','5d','5e','5f','5g','5h',
    #'6a','6b','6c','6d','6e','6f','6g','6h',
    #'7a','7b','7c','7d','7e','7f','7g','7h',
    #'8a','8b','8c','8d','8e','8f','8g','8h']
    
    #for i in range(len(mat)):
    #    print(mat[i])

    #dy = []

    # l = "00abcdefgh00"
    # c_l = cab[0]
    # c_n = int(cab[1])
    # tot = 0

    # # Mov izq
    # posible_l = l[l.index(c_l) - 2]
    # posible_n = c_n-1
    # posibl
    # if posible_l != 0 && posible_n > 0 && posible_n < 9:
    #     tot += 1