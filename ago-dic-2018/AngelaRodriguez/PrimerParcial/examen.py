
def conv_horas(hora): 
      
  
    if hora[-4:] == "A.M." and hora[:2] == "12": 
        return "00" + hora[2:5] + "hrs"
          
     
    elif hora[-4:] == "A.M.": 
        return hora[:-5] + "hrs"
      
    
    elif hora[-4:] == "P.M." and hora[:2] == "12": 
        return hora[:-5] + "hrs"
          
    else: 
          
       
        return str(int(hora[:2]) + 12) + hora[2:5] + "hrs"
  
         
print(conv_horas("02:23 P.M.")) 
print(conv_horas("11:42 P.M.")) 
print(conv_horas("11:42 A.M.")) 
print(conv_horas("12:00 A.M.")) 
print(conv_horas("12:00 P.M.")) 
print(conv_horas("01:05 A.M.")) 
print(conv_horas("11:59 P.M.")) 

