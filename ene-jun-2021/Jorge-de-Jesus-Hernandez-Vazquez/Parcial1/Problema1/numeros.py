

def numero_triangular(n: int):
    L = {} #Para guardar los valores
    T = (n * (n+1)/2) #Formula de los numeros triangulares
    for i in range(1, n+1):
        L[i] = T
        
    return int(L[i])
    
if __name__ == "__main__":
    print(numero_triangular(400))
        
       
         
 