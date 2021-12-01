
from interfaz import Escritor

class Escribir(Escritor):
    def escribir_cantidad_vocales(parametro:str):
        vocales=0
        for letra in parametro:
            if letra.lower() in"aeiou":
                vocales +=1
        return str(vocales)

if __name__ == '__main__':
    dato = input('Escribe tu libro favorito para contar las vocales:')
    print(Escribir.escribir_cantidad_vocales(dato))




