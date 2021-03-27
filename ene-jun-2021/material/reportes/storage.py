from entity import Alumno, Calificacion

def ObtenerAlumnos() -> list[Alumno]:
    # connect db
    return [Alumno("Juan", "102435432"), Alumno("Ana", "101231231"), Alumno("Lupita", "103234212"), Alumno("David", "106542326"), Alumno("Luis", "105432532"), Alumno("Chio", "10250277")]

def ObtenerCalif(alumno: Alumno) -> list[Calificacion]:
    return [Calificacion("Mate", 90), Calificacion("Español", 75), Calificacion("Ingles", 70)]