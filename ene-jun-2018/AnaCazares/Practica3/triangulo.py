
#//programa que determina tipo de triangulo

def Triangulo(): 
   lado=list(map(int,input("lado:").split()))
   if(lado[0]==lado[1] and lado[1]==lado[2]):
       print ("\nEl Triangulo es Equilatero")
   elif(lado[0]==lado[1] or lado[0]==lado[2] or lado[1]==lado[2]):
       print ("\nEl Triangulo es Isoceles")
   elif (lado[0]!=lado[1] or lado[0]!=lado[2] or lado[1]!=lado[2]):
       print( "\nEl Triangulo es Escaleno")
   else: print("no es triangulo")
       
 
if __name__ == '__main__':
    Triangulo()



   

