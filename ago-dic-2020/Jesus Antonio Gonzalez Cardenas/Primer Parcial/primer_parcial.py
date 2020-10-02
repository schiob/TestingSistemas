import csv
import math

def CheckEquilatero(x, y, z):
    if x == y and y == z:
        return True
    else:
        return False

def CheckIsoceles(x, y, z):
    if x == y or x == z or y == z:
        return True
    else:
        return False

def CheckEscaleno(x, y, z):
    if  CheckEquilatero(x, y, z) or CheckIsoceles(x, y, z):
        return False
    else:
        return True

def CheckNoEsTriangulo(x, y, z):
    if (x + y) > z and (x + z) > y and (y + z) > x:
       return False
    else:
        return True

def Tri_from_file(fpath:str):
    with open(fpath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        info =  [row for row in csv_reader]
        x = int(info[0][0])
        y = int(info[0][1])
        z = int(info[0][2])
 
    if CheckNoEsTriangulo(x, y, z):
        return 'No triángulo'
    if CheckEquilatero(x, y, z):
        return 'Equilátero'
    if CheckIsoceles(x, y, z):
        return 'Isóceles'
    if CheckEscaleno(x, y, z):
        return 'Escaleno'
    


if __name__ == "__main__":  
    FilePath = 'triangulo.txt'
    print(Tri_from_file(FilePath))
