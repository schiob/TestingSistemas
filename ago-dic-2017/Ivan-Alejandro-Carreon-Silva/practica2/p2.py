import sys

def imprimeFile(path):
    a = open(path)
    return a.read()

def escribeFile(path, str):
    a = open(path,'w')
    a.write(str)
    a.close()


if __name__ == '__main__':
    escribeFile("pedrito.txt","bulbasaur")
print(imprimeFile("pedrito.txt"))
