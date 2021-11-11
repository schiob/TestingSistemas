import os
def leer_archivo():
    f = open("ago-dic-2021\Javier Eduardo Aleman Ortiz\calificaciones.txt","r")
    for line in f:
        datos = [line.rstrip('\n').split(' ',maxsplit=3)]
        print(datos[0][0],datos[0][2])

class Escritor():

    def escribir(texto:str):
        file = open("Parcial_2\documento.txt", "w")
        file.write(texto + os.linesep)
        file.close()

if __name__ == "__main__":
    leer_archivo()
    Escritor.escribir(input("##########\n"))
