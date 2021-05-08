import os.path as path
import requests


def regretContent(nombre):
    if path.exists(nombre):
        f = open(f'{nombre}', 'r')
        mensaje = f.read()
        f.close()
        return mensaje
    else:
        ff = open('perrito.txt', 'r', encoding="utf8")
        p = ff.read()
        ff.close()
        return p


def palabras_arriba(cadena):
    response = requests.post("HTTP://API.SHOUTCLOUD.IO/V1/SHOUT", json={"INPUT": cadena})
    r = response.json()
    return r['OUTPUT']


def regretContentUP(cadena):
    contenido = regretContent(cadena)
    palabras = palabras_arriba(contenido)
    return palabras


def main():
    # Esta linea verifica que un archivo exista prueba_sp.txt
    # archivo2 = input('Dime el nombre de un archivo con todo y extencion -> ')
    # print(regretContent(archivo2))

    # Esta linea verifica que no existe
    # print(regretContent('prueba_spp.txt'))

    # este es para las palabras arriba
    # frase = input('Dime una frase que te guste mucho -> ')
    # print(palabras_arriba(frase))

    # este es para probar ambas funciones
    archivo = input('Dime el nombre de un archivo con todo y extencion -> ')
    print(regretContentUP(archivo))


if __name__ == '__main__':
    main()
