def cambio(cadena):
    horas = cadena[0] + cadena[1]  # las posiciones 0-1 del str me dan las hrs
    horasint = int(horas)  # transformo la horas a int
    minutos = cadena[3] + cadena[4]  # las posiciones 3-4 del str me dan los minutos
    minutosint = int(minutos)  # transformo los minutos en int

    if horasint < 12 and horasint >= 1:
            return (f"{horas}:{minutos}a.m.")

    if horasint == 12:
        return (f"{horas}:{minutos}p.m.")

    if horasint == 0 or horasint == 00:
        a = "12"
        return (f"{a}:{minutos}a.m.") #regresa 12 porque son las 12
    if horasint > 12 and horasint <= 23:
        if horasint == 13:
            c1 = "01"
            return (f"{c1}:{minutos}p.m.")
        if horasint == 14:
            c2 = "02"
            return (f"{c2}:{minutos}p.m.")
        if horasint == 15:
            c3 = "03"
            return (f"{c3}:{minutos}p.m.")
        if horasint == 16:
            c4 = "04"
            return (f"{c4}:{minutos}p.m.")
        if horasint == 17:
            c5 = "05"
            return (f"{c5}:{minutos}p.m.")
        if horasint == 18:
            c6 = "06"
            return (f"{c6}:{minutos}p.m.")
        if horasint == 19:
            c7 = "07"
            return (f"{c7}:{minutos}p.m.")
        if horasint == 20:
            c8 = "08"
            return (f"{c8}:{minutos}p.m.")
        if horasint == 21:
            c9 = "09"
            return (f"{c9}:{minutos}p.m.")
        if horasint == 22:
            c10 = "10"
            return (f"{c10}:{minutos}p.m.")
        if horasint == 23:
            c11 = "11"
            return (f"{c11}:{minutos}p.m.")
    if horasint == 24:
        b = "12"
        return (f"{b}:{minutos}a.m.")


if __name__ == '__main__':
    hora = input()
    print(cambio(hora))