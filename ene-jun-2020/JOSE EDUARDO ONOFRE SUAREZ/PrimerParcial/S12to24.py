
class Tiempo:
    def Hora(horita):
        
        Hora = horita
        Hora.split()
        N1 = int(Hora[0] + Hora[1])
        N2 = int(Hora[3] + Hora[4])
        ext = str(Hora[5] +"."+ Hora [7])

     
        if ext == 'p.m' and N1 == 1 and N2 <=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
        
        if ext == 'p.m' and N1 == 2 and N2 <=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
            x = converted
        
        if ext == 'p.m' and N1 == 3 and N2 <=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
        
        if ext == 'p.m' and N1 == 4 and N2 <=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
        
        if ext == 'p.m' and N1 == 5 and N2<=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
        
        if ext == 'p.m' and N1 == 6 and N2<=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
        
        if ext == 'p.m' and N1 == 7 and N2<= 9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
        
        if ext == 'p.m' and N1 == 8 and N2<=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
        
        if ext == 'p.m' and N1 == 9 and N2<=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
        
        if ext == 'p.m' and N1 == 10 and N2<=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1 +":"+ n2 + "hrs"
        
        if ext == 'p.m' and N1 == 11 and N2<=9:
            n1 = str(12 + N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            if ext == 'p.m' and N1 == 11 and N2>9:
                n1 = str(12 + N1)
                n2 = str(N2)
                converted = n1 +":"+ n2 + "hrs"
        
     
        if ext == 'p.m' and N1 == 12 and N2<=9:
            n1 = str(N1)
            n2 = str(N2)
            converted = n1+":"+"0"+n2 + "hrs"
        else:
            if ext == 'p.m' and N1 == 12 and N2>9:
                n1 = str(N1)
                n2 = str(N2)
                converted = n1+":"+n2 + "hrs"  

    
        return converted

       

       








if __name__ == "__main__":

    
    Time = str(input("Escriba la hora a convertir: "))
    #Time = '02:23p.m.'
    #Time.split()
    #print(Time)
    #N1 = int(Time[0] + Time[1])
    #N2 = int(Time[3] + Time[4])
    #print(N2)
    print(Tiempo.Hora(Time))

