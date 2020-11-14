def promedio():
    archivo = open("calificaciones.txt", "r")
    lineas = archivo.readlines()
    calificaciones = 0
    numero_calificaciones = 0
    for i in range(0, len(lineas)):
        datos = lineas[i].strip().split(' ')
        nombre = datos[0]
        materia = datos[1]
        calificacion = float(datos[2])
        numero_calificaciones += 1
        if i < len(lineas)-1:
            if nombre == lineas[i+1].strip().split(' ')[0]:
                calificaciones += calificacion+float(lineas[i+1].strip().split(' ')[2])
            else:
                print("{} {}".format(nombre, calificaciones/numero_calificaciones))
                calificaciones = 0
                numero_calificaciones = 0
        else:
            print("{} {}".format(nombre, calificaciones/numero_calificaciones))
            calificaciones = 0
            numero_calificaciones = 0

if __name__ == '__main__':
    promedio()