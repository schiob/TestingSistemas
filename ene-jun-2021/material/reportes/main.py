from storage import ObtenerAlumnos, ObtenerCalif
from report import genReport

def main(reportGenerator, promediador, genMensaje):
    # Obtener lista de alumnos
    alumnos = ObtenerAlumnos()

    # Presentar opciones y seleccionar un alumno
    print("selecciona un alumno, el número:")
    for i, alumno in enumerate(alumnos):
        print(i, alumno.nombre)

    select = int(input())

    # Obtener califas
    califs = ObtenerCalif(alumnos[select])

    # Generar reporte de alumno
    return reportGenerator(alumnos[select], califs, promediador, genMensaje)


if __name__ == "__main__":
    print(main(genReport))