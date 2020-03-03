import unittest
def hora12to24(Hora):
    if Hora[-4:]=="a.m.":
        if Hora[:2]=="12":
            Hora24="00"+Hora[2:-4:]+"hrs"
            return Hora24
        Hora24 = Hora[:-4]+"hrs"
        return Hora24
    elif Hora[-4:]=="p.m.":
        if Hora[:2]=="12":
            Hora24=Hora[:-4]+"hrs"
            return Hora24
        Hora24= str(int(Hora[:2]) + 12) + Hora[2:5]+"hrs" 
        return Hora24
