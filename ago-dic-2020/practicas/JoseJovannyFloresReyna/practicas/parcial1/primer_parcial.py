def tipoTriangulo(triangulo):
    
    #La suma de las longitudes de dos de los lados de un triangulo es mayor que 
    #la longitud del tercer lado, si no se cumple, no es un triangulo
    
    if triangulo[0] >= (triangulo[1] + triangulo[2]) or triangulo[1] >= (triangulo[0] + triangulo[2]) or triangulo[2] >= (triangulo[0] + triangulo[1]) or (triangulo[0]+triangulo[1]+triangulo[2])==0:
        return "No triangulo"
    
    #sus lados son iguales
    elif triangulo[0] == triangulo[1] == triangulo[2]:    
            return "Triangulo equilátero"
    
    #dos lados iguales
    elif triangulo[0] == triangulo[1] or triangulo[1] == triangulo[2] or triangulo[0] == triangulo[2]:    
            return "Isósceles"
    #lados diferentes    
    else:
        return "Escaleno"

if __name__ == "__main__":

    entrada = input()
    separador = entrada.split(" ")
    L1 = int(separador[0])
    L2 = int(separador[1])
    L3 = int(separador[2])

    triangulo = [L1, L2, L3]    
    


    print(tipoTriangulo(triangulo))

