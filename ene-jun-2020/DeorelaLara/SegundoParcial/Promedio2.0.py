import os
#Funcion para leer archivo
def ReadFile(path):
    file_name = open(path, 'r')
    content = file_name.readline()
    splt = content.split(',')
    file_name.close()
    return print(splt)
#Funcion para crear un archivo 
def mkFile(path):
    file_name = open(path, 'w')
    file_name.write('Jose_Lopez quimica 89.00, Jose_Lopez matematicas 85.34, Maria_Martinez fisica 95.50, Maria_Martinez espaÃ±ol 90.00')
    file_name.close()
    return print('Done')
#Funcion para eliminar 
def DeleteFile(path):
    os.remove(path)



if __name__ == '__main__':
    ReadFile('c:/Users/deore/OneDrive/Escritorio/Python/Calidad/test1.0.txt')
    mkFile('c:/Users/deore/OneDrive/Escritorio/Python/Calidad/test2.0.txt')
