def Time(s):
    formato = s [-2:]
    hora = s[:2]

    if formato == "AM":
        if hora == "12":
            return "00"+ s[2:-2]
        else:
            return s[:-2]
    elif hora == "12":
            return s [:-2]
    else:
            return (str(int(hora) + 12)+s[2:-2])

s= input().strip()
result= Time(s)

print (result)
