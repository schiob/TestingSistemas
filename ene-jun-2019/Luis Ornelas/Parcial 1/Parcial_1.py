def convertir24a12(str1):
    horas = int(str1[0:2])
    minutos = int(str1[3:5])

    if horas < 12 and horas >= 1:
            return (f"{horas}:{minutos}A.M.")

    if horas == 12:
        return (f"{horas}:{minutos}P.M.")

    if horas == 0 or horas == 00:
        a = "12"
        return (f"{a}:{minutos}A.M.")
    if horas > 12 and horas <= 23:
        if horas == 13:
            v1 = "01"
            return (f"{v1}:{minutos}P.M.")
        if horas == 14:
            v2 = "02"
            return (f"{v2}:{minutos}P.M.")
        if horas == 15:
            v3 = "03"
            return (f"{v3}:{minutos}P.M.")
        if horas == 16:
            v4 = "04"
            return (f"{v4}:{minutos}P.M.")
        if horas == 17:
            v5 = "05"
            return (f"{v5}:{minutos}P.M.")
        if horas == 18:
            v6 = "06"
            return (f"{v6}:{minutos}P.M.")
        if horas == 19:
            v7 = "07"
            return (f"{v7}:{minutos}P.M.")
        if horas == 20:
            v8 = "08"
            return (f"{v8}:{minutos}P.M.")
        if horas == 21:
            v9 = "09"
            return (f"{v9}:{minutos}P.M.")
        if horas == 22:
            v10 = "10"
            return (f"{v10}:{minutos}P.M.")
        if horas == 23:
            v11 = "11"
            return (f"{v11}:{minutos}P.M.")
    if horas == 24:
        b = "12"
        return (f"{b}:{minutos}A.M.")


if __name__ == '__main__':
    hora = input("Dame la Hora (HH:MM/hrs): ")
    print(convertir24a12(hora))