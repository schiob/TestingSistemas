#Escribe un pequeño programa que tome 2 números de STDIN y muestre el resultado de su suma.

if __name__ == "__main__":
    while True:
        numerosList = list(map(float, input("\nInserte dos numeros separados por espacios: \n").split())) 

        if len(numerosList) > 2:
            print('Inserte solo 2 numeros')
            continue
        else:
            print("\nResultado: ", sum(numerosList))
            break

    pass