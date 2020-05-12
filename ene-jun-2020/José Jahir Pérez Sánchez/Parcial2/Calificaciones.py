def calificar(file_name):
    file = open(file_name, "r")
    content = file.read()
    lista = []
    for palabra in content.split("\n"):
        lista.append(palabra.split(" "))
    contador1 = 0
    contador2= 0
    res=0
    for cosas in content:
        res+=float(lista[contador1][contador2+2])

    file.close
    return lista[0][0],round(res/len(content),2)

if __name__ == "__main__":
    print(calificar("alumnos.txt"))