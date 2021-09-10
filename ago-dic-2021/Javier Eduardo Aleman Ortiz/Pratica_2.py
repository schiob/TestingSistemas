def suma_Numeros(n1,n2):


    if isinstance(n1, (float,int) ) and isinstance(n2, (float,int)):
        return n1+n2

    return "error"

if __name__=="__main__":
    n1,n2=list(map(float,input().split()))
    print(suma_Numeros(n1,n2))