def Promedio():
    file = open("Calificaciones.txt", "r")
    lineas = file.readlines()
    
    #MATRIZ DE CALIFAS
    Alumno1 = ""
    Alumno2 = ""
    CalAlumno1Materia1 = 0.0
    CalAlumno1Materia2 = 0.0
    CalAlumno2Materia1 = 0.0
    CalAlumno2Materia2 = 0.0
    PromAlumno1 = 0.0
    PromAlumno2 = 0.0
    
    
    #CHECA QUE EN LA POSICION 0 DE LA LINEA 1 SEA LA LETRA J DE JORGE (NOMBRE)
    for i in lineas:
        if i[0] == "J":
            Alumno1 = i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]
        else:
            Alumno2 = i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]+i[10]+i[11]+i[12]+i[13]

    #CHECA EN LA PARTE DE LA MATERIA SI LA POSICION 11 ES Q "QUIMICA" Y M "MATEMATICAS" DEL ALUMNO 1 
    for ii in lineas:
        if ii[11] == "q":
            CalAlumno1Materia1 = ii[19]+ii[20]+ii[21]+ii[22]+ii[23]
        if ii[11] == "m":
            CalAlumno1Materia2 = ii[23]+ii[24]+ii[25]+ii[26]+ii[27]

    #CHECA EN LA PARTE DE LA MATERIA SI LA POSICION 15 ES F "FISICA" Y E "ESPAÑOL" DEL ALUMNO 2
    for iii in lineas:
        if iii[15] == "f":
            CalAlumno2Materia1 = iii[22]+iii[23]+iii[24]+iii[25]+iii[26]
        if iii[15] == "e":
            CalAlumno2Materia2 = iii[23]+iii[24]+iii[25]+iii[26]+iii[27]

    #CALCULAMOS PROMEDIO Y CONVERTIMOS LOS STRINGS A FLOATS
    CalAlumno1Materia1 = float(CalAlumno1Materia1)
    CalAlumno1Materia2 = float(CalAlumno1Materia2)
    PromAlumno1 = float(PromAlumno1)
    CalAlumno2Materia1 = float(CalAlumno2Materia1)
    CalAlumno2Materia2 = float(CalAlumno2Materia2)
    PromAlumno2 = float(PromAlumno2)
    PromAlumno1 = (CalAlumno1Materia1 + CalAlumno1Materia2)/2.0
    PromAlumno2 = (CalAlumno2Materia1 + CalAlumno2Materia2)/2.0


    return (f"{Alumno1} {PromAlumno1}" + f"\n{Alumno2} {PromAlumno2}")


def main():
    print(Promedio())


if __name__ == '__main__':
    main()