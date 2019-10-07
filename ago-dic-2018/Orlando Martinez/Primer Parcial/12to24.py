from datetime import datetime, date, time, timedelta
import calendar
def Hora(self,hora):
    Hora="%H:%M:%S"
    if Hora>("12:00:00"):
        Hora=Hora+12

if __name__ == '__main__':
    Hora=input("Ingrese hora: ")
    Formato=input("Ingrese formato:")
    resultado=(Hora)
    print("Hora {}".format(Hora))
