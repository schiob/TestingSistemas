
def numbers(L):
    pos = neg = par = impar = 0
     
    lista = L.split()
    for i in lista:
        i = int(i)
        
        if i % 2 == 0:
            par += 1
        
        if i % 2 != 0:
            impar += 1
        
        if i < 0:
            neg += 1
        
        if i > 0:
            pos += 1     
    
    return print(f"""{pos} número(s) positivo(s)\n{neg} número(s) negativo(s)\n{par} número(s) par(es)\n{impar} número(s) impar(es)""".strip())


if __name__ == "__main__":
    #L = list(map(int, input().split()))
    L = input()
    numbers(L)
