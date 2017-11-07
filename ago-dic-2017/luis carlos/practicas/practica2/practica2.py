def RegresaString(archivo):
    A=open(archivo)
    B = A.read()
    return B
    print(B)
    A.close()

def recibe(archivo,stri):
    x=open(archivo,"w")
    s=x.write(stri)
    return s
    s.close()

