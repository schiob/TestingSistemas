
class part1():

    def calificaciones(archivo):
        calificaciones = []
        for lineas in archivo:
            calificaciones.append(lineas.split())

        promedios = []
        promedio = 0
        califs = 0
        entero = 0
        pos = 0
        nombreTemp = calificaciones[0][0]

        for x in range(len(calificaciones)):
            if nombreTemp == calificaciones[pos][0]:
                califs += int(calificaciones[pos][2])
                pos = pos + 1
                entero = entero + 1
                promedio = (califs/entero)
            else:
                nombreTemp = calificaciones[pos][0]
                califs = int(calificaciones[pos][2])
                entero = 0
                entero = entero + 1
                promedio = (califs/entero)
            promedios.append([nombreTemp, "{0:.2f}".format(promedio)])
        return promedios
        # print(promedios)
