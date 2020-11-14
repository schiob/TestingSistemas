archivo = 'C:/Users/Crist/OneDrive/Escritorio/calificaciones.txt'
file = open(archivo, 'r')
contenido = file.readline()
splt = contenido.split(',')
file.close()
print (splt)

def calcular_promedio(list):
    alumno1 = splt[0]
    splt1 = alumno1.split(" ")
    alumno2 = splt[1]
    splt2 = alumno2.split(" ") 
    alumno3 = splt[2]
    splt3 = alumno3.split(" ")
    alumno4 = splt[3]
    splt4 = alumno4.split(" ")

    alumno1Promedio = (float(splt1[2]) + float(splt2[2]))/2
    alumno2Promedio = (float(splt3[2]) + float(splt4[2]))/ 2
    return '{} - {}\n{} - {}'.format(splt1[0], alumno1Promedio, splt3[0], alumno2Promedio)

if __name__ == '__main__':
    print(calcular_promedio(splt))