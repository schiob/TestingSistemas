def promedio():
    f = open("Informacion.txt", "r")
    lines = f.readlines()

    cal1 = 0.0
    cal12 = 0.0
    cal21 = 0.0
    cal22 = 0.0
    prom1 = 0.0
    prom2 = 0.0
    alumno1 = ""
    alumno2 = ""
    a1 = 0

    for i in lines:
        if i[0] == "J":
            alumno1 = i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]
        else:
            alumno2 = i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]+i[10]+i[11]+i[12]+i[13]

    for j in lines:
        if j[11] == "q":
            cal1 = j[18]+j[19]+j[20]+j[21]+j[22]+j[23]
        if j[11] == "m":
            cal12 = j[23]+j[24]+j[25]+j[26]+j[27]+j[28]

    for k in lines:
        if k[15] == "f":
            cal21 = k[22]+k[23]+k[24]+k[25]+k[26]
        if k[15] == "e":
            cal22 = k[22]+k[23]+k[24]+k[25]+k[26]+k[27]

    cal12 = float(cal12)
    cal1 = float(cal1)
    prom1 = float(prom1)
    cal21 = float(cal21)
    cal22 = float(cal22)
    prom1 = float(prom1)
    prom1 = (cal1 + cal12)/2.0
    prom2 = (cal21 + cal22)/2.0

    return f"{alumno1} {prom1}" + f"\n{alumno2} {prom2}"


def main():
    print(promedio())


if __name__ == '__main__':
    main()
