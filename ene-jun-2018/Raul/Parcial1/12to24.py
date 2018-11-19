import time 
import datetime



def CambioHora(hora12,minutos):
    
    hora24 = hora12 + 12
  
    t2 = datetime.time(hora24, minutos)
   



    return t2
        
    
    







if __name__== "__main__":
    
    entrada= []
    entrada = input("Hora: ").split(":")
    hora12 = int(str(entrada[0]))
    minutos = int(str(entrada[1]))
    ok = CambioHora(hora12,minutos)
    print(ok)
    
