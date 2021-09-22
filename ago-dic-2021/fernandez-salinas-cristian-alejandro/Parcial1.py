import unittest

def taquitos(orden):
    orden = list(map(str,orden.split()))
    cachete = 0
    lengua = 0
    tripitas = 0
    pastor = 0
    machito = 0

    if len(orden) >= 30:
        return("Error son demaciados taquitos")

    for i in range(len(orden)):
        if orden[i] == "cachete":
            cachete += 1
        elif orden[i] == "lengua":
            lengua += 1
        elif orden[i] == "tripitas":
            tripitas += 1
        elif orden[i] == "pastor":
            pastor += 1
        elif orden[i] == "machito":
            machito += 1
        else:
            return("Hay un taquito que no existe en el menu")
    
    res = (cachete * 13 + lengua * 10 + tripitas * 9 + pastor * 15 + machito * 14)
    print(res)
    return res

if __name__ == '__main__':
    orden = input("Digame que taquitos va a querer")
    taquitos(orden)
