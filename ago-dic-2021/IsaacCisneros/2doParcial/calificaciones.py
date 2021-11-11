
archivito = 'C:\Users\isaac\OneDrive\Documentos\TestingSistemas\ago-dic-2021\IsaacCisneros\2doParcial\calificaciones.txt'
file = open(archivito, 'r')
contenido = file.readline()
splt = contenido.split(',')
file.close()
print (splt)

def calcular_promedio(list):
    a11 = splt[0]
    splt1 = a11.split(" ")
    a12 = splt[1]
    splt2 = a12.split(" ") 
    a21 = splt[2]
    splt3 = a21.split(" ")
    a22 = splt[3]
    splt4 = a22.split(" ")

    a1Promedio = (float(splt1[0]) + float(splt2[1]))/2
    a2Promedio = (float(splt3[2]) + float(splt4[3]))/ 2
    return '{} - {}\n{} - {}'.format(splt1[0], a1Promedio, splt3[0], a2Promedio)

if __name__ == '__main__':
    print(calcular_promedio(splt))