# Función para obtener el promedio dado lo sdatos de un archivo.
# Sorry, me la compliqué mucho, no había notado que decía: Todas las calificaciones de un alumno están siempre seguidas. De lo contrario no hubiera hecho tanto desmadre LOL sorry.
def obtener_promedio(archivo):
    lista_alumnos = archivo.readlines()
    # Se genera un diccionario con el nombre de los estudiantes.
    alumnos = { alumno.strip().split(' ')[0] : { 'total' : 0, 'materias' : 0 } for alumno in lista_alumnos}
    # Se actualiza el diccionario. Cada estudiante tendrá otro diccionario con la cantidad de materias que cursa y el total de estas.
    for alumno in lista_alumnos:
        datos = alumno.strip().split(' ')
        alumnos.update(
            {
                datos[0] : 
                    {
                        'total' : alumnos[datos[0]]['total'] + float(datos[2]), 
                        'materias' : alumnos[datos[0]]['materias']+1
                    }
            }
        )
    # Se retorna el resultado.
    resultado = ""
    for nombre, valores in alumnos.items():
        # Fue necesario usar el format de decimales porque a veces podía dar 100.0 en lugar de 100.00 dadas ciertas condiciones por si gustas checarlas:
        # Un caso de ellos es cuando un alumno tiene sólo una materia por ejemplo, pero con este hotfix ya queda siempre.
        resultado += "{} {}\n".format(nombre, '{:.2f}'.format(valores['total']/valores['materias']))
    return resultado.rstrip("\n")