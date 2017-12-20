def printFile(path):
    archivo = open(path)
    return archivo.read()

def writeFile(path, string):
    archivo = open(path,'w')
    archivo.write(string)
    archivo.close()

if __name__ == '__main__':
    writeFile("gomes.txt","charmander")
    print(printFile("gomes.txt"))
