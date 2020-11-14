def Promedio():
    archivo = open("calificaciones.txt", 'r')
    contenido = archivo.readlines()

   
    
    Alumno1 = ""
    CalQuimica = 0.0
    CalMatematicas = 0.0
    PromAlumno1 = 0.0
    
    Alumno2 = ""
    CalFisica = 0.0
    CalEspañol = 0.0
    PromAlumno2 = 0.0
    
    
    for i in contenido:
        if i[0:10] == "Jose_Lopez":
            Alumno1 = i[0:10]
        else:
            Alumno2 = i[0:14]
            
    for j in contenido:
        if j[11:18] == "quimica":
            CalQuimica = j[19:23]
        if j[11:22] == "matematicas":
            CalMatematicas = j[23:27]

    #CHECA EN LA PARTE DE LA MATERIA SI LA POSICION 15 ES F "FISICA" Y E "ESPAÑOL" DEL ALUMNO 2
    for h in contenido:
        if h[15:21] == "fisica":
            CalFisica = h[22:26]
        if h[15] == "e": #español
            CalEspañol = h[23:27]

    #CALCULAMOS PROMEDIO Y CONVERTIMOS LOS STRINGS A FLOATS
    CalQuimica = float(CalQuimica)
    CalMatematicas = float(CalMatematicas)
    PromAlumno1 = float(PromAlumno1)
    CalFisica = float(CalFisica)
    CalEspañol = float(CalEspañol)
    PromAlumno2 = float(PromAlumno2)
    PromAlumno1 = float(CalQuimica + CalMatematicas)/2.0
    PromAlumno2 = float(CalFisica + CalEspañol)/2.0
    
    return (f"{Alumno1} {PromAlumno1}" + f"\n{Alumno2} {PromAlumno2}")


def main():
    print(Promedio())


if __name__ == '__main__':
    main()
    