def average():
    grade = 0
    i = 0
    doc = open('calificaciones.txt', 'r')

    data = doc.read().splitlines()
    for linea in data:
        degree = data[0][-5:]
        grade +=float(degree)
        i = i+1

    if i == 0:
        return 'No hay calificaciones'
    return  grade/i

if __name__ == "__main__":
    print(average())