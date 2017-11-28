def main(#variable para leer un archivo que no sea fijo):
    archivo = open("/Users/Georgina/Desktop/archivo.txt")
    leer= archivo.read()
    leer.split(" ")
    a,b,c=leer.split(" ")  
    archivo.close()
        
    if (a!=0) or (b!=0) or (c!=0):
        if(a==b==c):#todos los lados son iguales
            print ("Equilatero")
        if(a==b or a==c or b==c):#solo 2 lados son iguales
            print ("Isosceles")
        else: print ("Escaleno")#ningun lado es igual

    else:print ("No triangulo")
    
main()
    
