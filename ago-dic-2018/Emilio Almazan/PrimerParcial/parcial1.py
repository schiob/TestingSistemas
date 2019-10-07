import sys

def convertor(t):
    formato = t[-2:]
    hora = t[:2]

    if formato == "AM":
        if hora == "12":
            return "00" + t[2:-2]
        else:
            return t[:-2]
    elif hora == "12":
        return t[:-2]
    else:
        return (str(int(hora) + 12) + t[2:-2])

if __name__ == '__main__':
    t = input("Dame el tiempo a convertir con formato AM o PM: ").strip()
    resultado = convertor(t)+("Hrs")

    print(resultado)
