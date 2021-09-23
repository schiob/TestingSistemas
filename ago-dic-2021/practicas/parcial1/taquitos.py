def tacosCheco(menu):
    cachete = 0
    lengua = 0
    tripita = 0
    pastor = 0
    machito = 0
    total = 0

    for taco in menu:
        if(taco == "cachete"):
            cachete += 1
        elif(taco == "lengua"):
            lengua += 1
        elif(taco == "tripita"):
            tripita += 1
        elif(taco == "pastor"):
            pastor += 1
        elif(taco == "machito"):
            machito += 1

    total = (cachete*13)+(lengua*10)+(tripita*9)+(pastor*15)+(machito*14)
    print(f'{cachete} cachete, {lengua} lengua, {tripita} tripita, {pastor} pastor {machito} machito')

    print(f"total {total}")

    return total
if __name__ == '__main__':
    print("¿Qué va a llevar güerito?")
    orden = list(map(str, input().split()))
    print(tacosCheco(orden))