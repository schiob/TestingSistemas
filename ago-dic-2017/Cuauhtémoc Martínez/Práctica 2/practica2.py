import sys

def printFile(path):
    # Se abre archivo (default modo lectura) y se asigna a f.
    f = open(path)
    # f.read() lee todo lo restante del archivo, en este caso TODO el archivo.
    return f.read()

def writeFile(path, str):
    # Se abre el archivo en modo escritura.
    f = open(path,'w')
    # write() sobreescribe el archivo, si no existe lo crea.
    f.write(str)


if __name__ == '__main__':
    writeFile("test.txt","charmander")
    print(printFile("test.txt"))
