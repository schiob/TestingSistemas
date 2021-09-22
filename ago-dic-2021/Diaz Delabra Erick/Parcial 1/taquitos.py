def taquitosClase(esperado):
    total = 0
    tamaño = len(esperado)

    if tamaño <= 30 :
        for i in esperado:
            if i == "cachete":
                total = total + 13
                
            elif i == "lengua":
                total = total + 10

            elif i == "tripitas":
                total = total + 9

            elif i == "pastor":
                total = total + 15

            elif i == "machito":
                total = total + 14

    return (total)

if __name__ == "__main__":
    esperado = []
    num = int(print("Ingrese el tamaño de la lista (de 0 a 30)"))
    for i in range(num):
        i = input(f"Ingrese el taco pos(" + [i] + "):")
        esperado.append(i)