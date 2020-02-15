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

if __name__ == "__main__":
    calcular_mov()
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