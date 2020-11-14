def calcular_promedio(filepath: str) -> dict:
    with open(filepath) as reader:
        content = [[i for i in student.split()] for student in reader.read().splitlines()]

    if len(content) == 1:
        return {}
    
    content = [[i[0],i[-1]]  for i in content]
    
    for student in content:
        if not student[-1].split(".")[0].isdigit():
            raise ValueError("Calificacion tiene que ser un numero positivo con decimales")

  
    estudiantes = {i: [] for i in {i[0] for i in sorted(content)}}
    for estudiante in estudiantes.keys():
        for e, cal in content:
            if e == estudiante:
                estudiantes[estudiante].append(float(cal))

    for k,v in estudiantes.items():
        estudiantes[k] = (sum(v)/len(v))

    return estudiantes


if __name__ == "__main__":
    for k,v in calcular_promedio("calificaciones.txt").items():
        print(k, v)