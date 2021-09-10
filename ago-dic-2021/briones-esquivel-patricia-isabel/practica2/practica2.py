# Modificar práctica 1 para hacer pruebas unitarias 
def sumar_dos_numeros(x,y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    
    return "error"

if __name__ == '__main__':
    x, y = list (map(int, input().split()))
    print(sumar_dos_numeros(x,y))