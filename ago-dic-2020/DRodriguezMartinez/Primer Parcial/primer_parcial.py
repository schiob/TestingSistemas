def Tri_from_file(filepath: str) -> str:
    def triangleInequality(a,b,c):

        if a + b > c and b + c > a and a + c > b:
            return True
        else:
            return False   
     ######

    with open(filepath) as reader:
        content = reader.read()

    a,b,c = [int(i) for i in content.split()]
    if triangleInequality(a,b,c):
        if a == b == c: return "Equilátero"
        if a == b or a == c or b == c: return "Isóceles"
        if (a != b != c): return "Escaleno"

    return "No triángulo"

###
if __name__ == "__main__":
    print(Tri_from_file("triangulo.txt"))