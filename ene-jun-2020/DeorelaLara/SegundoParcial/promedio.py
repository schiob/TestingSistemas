

file_name = 'c:/Users/deore/OneDrive/Escritorio/Python/Calidad/test1.0.txt'
file = open(file_name, 'r')
content = file.readline()
splt = content.split(',')
file.close()
print(splt)

def Promedio(list):
    #Calificaciones Alumno 1
    Stud1 = splt[0]
    splt1 = Stud1.split(" ")
    Stud2 = splt[1]
    splt2 = Stud2.split(" ") 
    #Calificaciones Alumno 2
    Stud3 = splt[2]
    splt3 = Stud3.split(" ")
    Stud4 = splt[3]
    splt4 = Stud4.split(" ")

    JosePromedio = (float(splt1[2]) + float(splt2[2]))/2
    #print(JosePromedio)
    MariaPromedio = (float(splt3[2]) + float(splt4[2]))/ 2
    #print(MariaPromedio)
    return '{} - {}\n{} - {}'.format(splt1[0], JosePromedio, splt3[0], MariaPromedio)


if __name__ == '__main__':
    print(Promedio(splt))