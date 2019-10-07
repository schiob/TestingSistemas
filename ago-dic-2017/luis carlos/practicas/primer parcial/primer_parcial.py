
import math
def RegresaString(archivo):
    x=[]
    f=open(archivo)
    x=f.read().split()
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    
        
    if((abs(a-c)<b)and(b<(a+c))):
        pass
            
        if(a==b and a==c):
            return 'equilatero'
                 
        elif(a==b or a==c or b==c):
            return 'isoceles'
                
        elif(a!=b or a!=c or b!=c):
            return 'escaleno'
            
                            
    elif(a==0 or b==0 or c==0):
        return'no triangulo'
    else:
            
        return 'no triangulo'


    
resultado=RegresaString("texto.txt")
print(resultado)










