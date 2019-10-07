
def conversor(hora):
    hora12 = []
    for i in hora:
        hora12.append(i)
    if (hora12[5]=='p'):
        hora12[0]+=1
        hora12[1]+=2
    print(hora12)
    return hora12

if __name__ == '__main__':

    hora=(input('Hora en formato 12 horas: \n'))
    res=conversor(hora)
