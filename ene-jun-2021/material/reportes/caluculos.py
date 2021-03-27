from entity import Calificacion

def CalcPromedio(califs: list[Calificacion]) -> float:
    suma = 0
    for c in califs:
        suma += c.calificacion
    
    return suma / len(califs)