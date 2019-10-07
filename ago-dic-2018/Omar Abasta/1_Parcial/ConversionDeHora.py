import sys

def ConversionHora(s):
    formato = s[-2:]
    th = s[:2]

    if formato == 'AM':
        if  th == '12':
            return "00" + s[2:8]
        else:
            return s[:-2]
    elif th == '12':
            return s[:-2]
    else:
            i = int(th) + 12
            return  str(i) + s[2:8] #la variable i se vconvierte en string para poder hacer la concatencacion de min y seg



s = input().strip()
result = ConversionHora(s)
print(result)
