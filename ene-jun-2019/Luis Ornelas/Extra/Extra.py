def Impares(enter):
    length = enter.split()
    numero_1 = int(length[0])
    numero_2 = int(length[1])

    if numero_1 - numero_2 >= -1 and numero_1 - numero_2 <= 1:
        return 0
    else:
        up = 0
        down = 0
        sum = 0
        if numero_1 > numero_2:
            up = numero_1
            down = numero_2
        else:
            up = numero_2
            down = numero_1
        for i in range(down+1, up):
            if i%2 != 0:
                sum += i
        return sum

if __name__ == "__main__":
    imp = Impares('12 15')
    print(imp)
