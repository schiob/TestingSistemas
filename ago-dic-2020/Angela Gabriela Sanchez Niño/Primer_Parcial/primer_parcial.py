def triangulo(path):
    with open("datos.txt", "r") as archivo:
        archivo = open(path)
        data= list(map(int, archivo.read().strip().split(' ')))
        lado_a = data[0]
        lado_b = data[1]
        lado_c = data[2]

    if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a: #verificar que sea un triangulo
        if (lado_a == lado_b == lado_c): #todos los lado iguales
            return 'Equilatero'
        elif (lado_a == lado_b or lado_a == lado_c or lado_b == lado_c): #dos de sus lados iguales
            return 'Isosceles'
        else:
            return 'Escaleno' #todos los lados diferentes
    else:
        return 'No es triangulo'
    archivo.close()



if __name__ == '__main__':
    print(triangulo("datos.txt"))

