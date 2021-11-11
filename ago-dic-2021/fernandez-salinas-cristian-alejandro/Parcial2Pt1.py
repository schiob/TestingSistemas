def leerArch () -> str:
    archivo = open("datos.txt", "r")
    lineas = archivo.read()
    alumno = lineas.split('\n')
    calif = 0
    promediotxt = ""
    prom = 0
    if lineas == "":
        promediotxt = "No hay datos"
        return promediotxt
    else:
        for i in range(0,len(alumno), 1):
            temp = alumno[i].split(' ')
            if i == 0:
                temp2 = temp[0]
                contador = 0
            if temp2 != temp[0]:
                prom = calif / float(contador)
                promediotxt = promediotxt + temp2 + " " + str(prom) + "\n"
                calif = 0
                contador = 0
                temp2 = temp[0]
            if temp2 == temp[0]:
                contador+=1
                calif = calif + float(temp[2])
        prom = calif / float(contador)
        promediotxt = promediotxt + temp2 + " " + str(prom)

        return promediotxt