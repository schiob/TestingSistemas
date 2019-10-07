# Leer / escribir archivos.

# Escribe sobre un archivo con el contenido que llega de parámetro.
def write_file(path, content):
    f = open(path, 'w')
    f.write(content)

# Lee un archivo.
def read_file(path):
    f = open(path, 'r')
    return f.read()


if __name__ == '__main__':
    print(read_file('testfile.txt'))
