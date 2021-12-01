class Alumnos:
    def alumno(self):
        archivo = open('ago-dic-2021\JESUS SALVADOR DE LA CRUZ DAVILA\EXAMEN_SEGUNDO_PARCIAL\PARTE_1\calificiones.txt', 'r')
        total = 0
        contenido = archivo.read().splitlines()
        for linea in contenido:
            calificaciones = contenido[0][-5:]
            total += float(calificaciones)
        return float(total)/len(contenido)

if __name__ == '__main__':
    alu = Alumnos()
    print(alu.alumno())