
#//programa que determina tipo de triangulo

def Triangulo(): 
   lado=list(map(int,input("lado:").split()))
   if(lado[0]>0) and(lado[0]<=100) and (lado[1]>0) and(lado[1]<=100) and (lado[2]>0) and(lado[2]<=100):

      if(lado[0]+lado[1]>lado[2]) and (lado[2]+lado[3]>lado[1]) and (lado[3]+lado[1]>lado[2]):
         if (lado[0]==lado[1] and lado[1]==lado[2]):
            print ("\nEl Triangulo es Equilatero")
         elif(lado[0]==lado[1] or lado[0]==lado[2] or lado[1]==lado[2]):
            print ("\nEl Triangulo es Isoceles")
         elif (lado[0]!=lado[1] or lado[0]!=lado[2] or lado[1]!=lado[2]):
            print( "\nEl Triangulo es Escaleno")
      print("no es triangulo")
       
   else: print("sobrepasa rango")
if __name__ == '__main__':
    Triangulo()



