
def taquitos_sabrositos(tacos):
    cachete=0
    lengua=0
    tripitas=0
    pastor=0
    machito=0
    total=0

    for taquito in tacos:
        if(taquito == 'cachete' ):
            cachete +=1
        elif(taquito  =="lengua"):
            lengua+=1
        elif(taquito  =="tripitas"):
            tripitas+=1
        elif(taquito =="pastor"):
            pastor+=1
        elif(taquito =="machito"):
            machito+=1

    total = (cachete*13)+(lengua*10)+(tripitas*9)+(pastor*15)+(machito*14)

    return total


if __name__ == '__main__':
    print('ingresa tus taquitos')
    tacos = list(map(str, input().split()))
    print(taquitos_sabrositos(tacos))