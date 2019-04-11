def promedio():
    f = open("Alumnos_Calificaciones.txt", "r")
    linea = f.readlines()
    cal1 = 0.0
    cal2 = 0.0
    cal3 = 0.0
    cal4 = 0.0
    prom1 = 0.0
    prom2 = 0.0
    al1 = ""
    al2 = ""
    a1 = 0
    for i in linea:
        if i[0] == "K":
            al1 = i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]
        else:
            al2 = i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]+i[10]+i[11]+i[12]+i[13]
    for ii in linea:
        if ii[11] == "r":
            cal1 = ii[18]+ii[19]+ii[20]+ii[21]+ii[22]+ii[23]
        if ii[11] == "s":
            cal2 = ii[23]+ii[24]+ii[25]+ii[26]+ii[27]+ii[28]
    for iii in linea:
        if iii[15] == "f":
            cal3 = iii[22]+iii[23]+iii[24]+iii[25]+iii[26]
        if iii[15] == "e":
            cal4 = iii[22]+iii[23]+iii[24]+iii[25]+iii[26]+iii[27]
    cal2 = float(cal2)
    cal1 = float(cal1)
    prom1 = float(prom1)
    cal3 = float(cal3)
    cal4 = float(cal4)
    prom1= float(prom1)
    prom1 = (cal1 + cal2)/2
    prom2 = (cal3 + cal4)/2
    return (f"{al1} {prom1}" + f"\n{al2} {prom2}")

if __name__ == '__main__':
    print(promedio())