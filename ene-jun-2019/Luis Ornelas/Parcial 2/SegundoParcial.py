def Alumnos():
    a = open("alumnos.txt", "r")
    lineas = a.readlines()

    calif1 = 0.0
    calif12 = 0.0
    calif21 = 0.0
    calif22 = 0.0
    prom1 = 0.0
    prom2 = 0.0
    alumno1 = ""
    alumno2 = ""
    a1 = 0

    for i in lineas:
        if i[0] == "J":
            alumno1 = i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]
        else:
            alumno2 = i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]+i[10]+i[11]+i[12]+i[13]

    for ii in lineas:
        if ii[11] == "q":
            calif1 = ii[18]+ii[19]+ii[20]+ii[21]+ii[22]+ii[23]
        if ii[11] == "m":
            calif12 = ii[23]+ii[24]+ii[25]+ii[26]+ii[27]+ii[28]

    for iii in lineas:
        if iii[15] == "f":
            calif21 = iii[22]+iii[23]+iii[24]+iii[25]+iii[26]
        if iii[15] == "e":
            calif22 = iii[22]+iii[23]+iii[24]+iii[25]+iii[26]+iii[27]

    calif12 = float(calif12)
    calif1 = float(calif1)
    prom1 = float(prom1)
    calif21 = float(calif21)
    calif22 = float(calif22)
    prom1 = float(prom1)
    prom1 = (calif1 + calif12)/2.0
    prom2 = (calif21 + calif22)/2.0
    return ("{} {}" + "\n{} {}").format(self.alumno1, self.prom1, self.alumno2, self.prom2)

def main():
    print(Alumnos())

if __name__ == '__main__':
    main()