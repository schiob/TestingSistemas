def convertidor12to24(hora):
    hrs = int(hora[0:2])
    min = str(hora[3:5])
    pa= str(hora[5])

    if pa == "p" and hrs == 12:
        return(f"{hrs}:{min}hrs")

    if pa == "a" and hrs == 12:
        b = "00"
        return(f"{b}:{min}hrs")

    if pa == "p":
        hrs+=12
        return(f"{hrs}:{min}hrs")
       
    if pa == "a":
        if hrs == 1:
            a1 = "01"
            return(a1+f":{min}hrs")
        if hrs == 2:
            a2 = "02"
            return(a2+f":{min}hrs")
        if hrs == 3:
            a3 = "03"
            return(a3+f":{min}hrs")
        if hrs == 4:
            a4 = "04"
            return(a4+f":{min}hrs")
        if hrs == 5:
            a5 = "05"
            return(a5+f":{min}hrs")
        if hrs == 6:
            a6 = "06"
            return(a6+f":{min}hrs") 
        if hrs == 7:
            a7 = "07"
            return(a7+f":{min}hrs")
        if hrs == 8:
            a8 = "08"
            return(a8+f":{min}hrs")
        if hrs == 9:
            a9 = "09"
            return(a9+f":{min}hrs")
    
        return(f"{hrs}:{min}hrs")
if __name__ == "__main__":
        print(convertidor12to24("01:05a.m"))

