#Mostrar el archivo de calificaciones
def promedio():
    f = open("calificaciones.txt", "r")
    lineas = f.readlines()

    cal1 = 0.0
    cal12 = 0.0    cal21 = 0.0
    cal22 = 0.0
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
            cal1 = ii[18]+ii[19]+ii[20]+ii[21]+ii[22]+ii[23]
        if ii[11] == "m":
            cal12 = ii[23]+ii[24]+ii[25]+ii[26]+ii[27]+ii[28]

    for iii in lineas:
        if iii[15] == "f":
            cal21 = iii[22]+iii[23]+iii[24]+iii[25]+iii[26]
        if iii[15] == "e":
            cal22 = iii[22]+iii[23]+iii[24]+iii[25]+iii[26]+iii[27]

    #Promedio
    cal12 = float(cal12)
    cal1 = float(cal1)
    prom1 = float(prom1)
    cal21 = float(cal21)
    cal22 = float(cal22)
    prom1 = float(prom1)
    prom1 = (cal1 + cal12)/2.0
    prom2 = (cal21 + cal22)/2.0


    return (f"{alumno1} {prom1}" + f"\n{alumno2} {prom2}")


def main():
    print(promedio())


if __name__ == '__main__':
    main() 
