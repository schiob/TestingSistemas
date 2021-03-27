from entity import Alumno, Calificacion
from caluculos import CalcPromedio
from mensaje import MensajeBonito

def genReport(alumno: Alumno, califas: list[Calificacion], promediador, genMensaje) -> str:
    # Calcular promedio
    promedio = promediador(califas)

    # Generar mensaje agresivo 
    mensajito = genMensaje()

    # formatear el reporte
    calif_txt = ""
    for calif in califas:
        calif_txt += f"{calif.materia} {calif.calificacion}\n"

    reporte = f'''REPORTE
El alumno {alumno.nombre} tiene las sig calificaciones:
{calif_txt}
Con un promedio de {promedio}

GRACIAS
{mensajito}
'''


    return reporte


if __name__ == "__main__":
    print(genReport(Alumno("chio", "10250277"), [Calificacion("compiladores", 80), Calificacion("Algoritmos", 70)], CalcPromedio, MensajeBonito))