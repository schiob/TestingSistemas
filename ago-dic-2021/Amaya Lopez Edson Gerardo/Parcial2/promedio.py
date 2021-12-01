
def promedio():
    i=0
    calif=0
    archivo = open('calificaciones.txt', 'r')
    # contenido = archivo.read().split()
    contenido = archivo.read().splitlines()
    for linea in contenido:
        calificacion = contenido[0][-5:]
        calif +=float(calificacion)
        i=i+1

    if i ==0:
        return 'el alumno no tiene calificaciones'
    return  calif/i


if __name__ == "__main__":
    print(promedio())
