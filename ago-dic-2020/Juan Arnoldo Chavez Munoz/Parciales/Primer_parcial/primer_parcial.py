def Tri_from_file(path) -> str:
    file = open(path)
    data = file.read()
    print(data)
     
    #lo organizo en variables
    if len(data.split(" ")) == 3:
        a,b,c= data.split(" ")
        print(a)
        print(b)
        print(c)
    else:
        return "No es triangulo"
    #Comprobamos los lados

    if a == b and a == c:
        return "Es equilatero"
    if a == b and a !=c or b == c and b != a or c == a and a != b:
        return "Es iscoceles"
    else:
        return "Es Escaleno"



if __name__ == "__main__":
    #calculamos con el arhcivo    
    print(Tri_from_file("lados_cuad.txt"))
    
