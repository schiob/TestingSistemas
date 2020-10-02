import pandas

def tri_from_file(archivocsv) -> str:
    archivo = pandas.read_csv(archivocsv)

    datos = archivo.values.tolist()

    if datos[0][0] == 0 or datos[0][1] == 0 or datos[0][2] == 0:
        return "No triángulo"

    if datos[0][0] == datos[0][1] and datos [0][0] == datos[0][2] and datos[0][1] == datos[0][2]:
        return "Equilátero"

    if datos[0][0] == datos[0][1] or datos[0][0] == datos[0][2] or datos[0][1] == datos[0][2]:
        return "Isóceles"

    return "Escaleno"

triangulo = tri_from_file("ejemplo_examen.csv")
print(triangulo)