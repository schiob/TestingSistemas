
class escritor():    
    def escribir(string : str) -> str:
        return string

class implementacion(escritor):
    def escribir(string: str):
        string = input('Introduce dos numeros enteros separados por espacio')
        lista = string.split(' ')
        return str(int(lista[0]) + int(lista[1]))

class cliente():
    print(cliente1 = implementacion().escribir())

if __name__ == '__main__':
    cliente = cliente()
