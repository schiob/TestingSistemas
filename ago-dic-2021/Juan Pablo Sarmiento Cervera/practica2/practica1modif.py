def suma(m,n):
    if isinstance(m, int) & isinstance(n, int): 
        return m+n

    return "error"     
    #n1=int(input("Ingresa el primer valor entero que quieres sumar: "))
    #n2=int(input("Ingresa el segundo valor entero que quieres sumar: "))
    
    sum = int("m") + int("n")

    return sum
if __name__ == '__main__':
    suma1 = input()  
    suma2 = input() 
    print (suma(suma1,suma2))