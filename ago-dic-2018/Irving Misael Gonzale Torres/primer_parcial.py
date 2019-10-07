def convert24(str1): 
      
    if str1[-4:] == "A.M" and str1[:2] == "12": 
        return "00" + str1[2:5] 
    
    elif str1[-4:] == "A.M": 
        return str1[:-5]      
   
    elif str1[-4:] == "P.M" and str1[:2] == "12": 
        return str1[:-5]          
    else:          
        return str(int(str1[:2]) + 12) + str1[2:5] 

print(convert24("02:23P.M"))
print(convert24("11:42P.M"))
print(convert24("11:42A.M"))
print(convert24("12:00A.M"))
print(convert24("12:00P.M"))
print(convert24("01:05A.M"))
print(convert24("11:59P.M"))

