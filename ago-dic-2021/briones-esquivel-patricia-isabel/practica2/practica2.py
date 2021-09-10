def sumar_dos_numeros (a,b):
    if isinstance (a,int) and isinstance(b,int):
        return a+b

    return "error"

if __name__ == "__main__":
    a,b = list(map(int,input().split()))
    print(sumar_dos_numeros(a,b))