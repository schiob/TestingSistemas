def promedio(calif):
    '''promedio es una función que recibe una lista de calificaciones y regresa su promedio'''
    prom = sum(calif) / len(calif)
    return prom

if __name__ == '__main__':
    calificaciones = list(map(int, input().split()))
    resultado = promedio(calificaciones)
    print(resultado)
