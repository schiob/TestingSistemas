import csv
from io import StringIO

def calculo_de_promedio(archivo_csv):

    with open(archivo_csv, newline = '' ) as archivoE:
        reader = csv.reader(archivoE)
        for campo in reader:
            print(campo['usuario'], campo['correo'], campo['puntos'])

if __name__ == '__main__':
    calculo_de_promedio()
