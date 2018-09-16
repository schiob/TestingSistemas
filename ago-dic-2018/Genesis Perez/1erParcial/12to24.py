from datetime import datetime, time

def hora24(hora):
    formato24 = "%H:%M"
    hora24 = hora
    horaformato24 = hora24.strptime(formato24)
    return horaformato12 + "hrs"

if __name__ == '__main__':
    formato12 = "%I:%M %p"
    h = input("Introduce la hora en formato de 12 horas (HH:MM am/pm): ")
    hf12 = h
    horaformato12 = hf12.strptime(formato12)

    resultado = hora24(horaformato12)

    print("{}".format(resultado))
