def clasificar_num (lista:list):
    numpar = 0
    numimp = 0
    numpos = 0
    numneg = 0
    result = []
    for i in range(len(lista)):
        numero = int(lista[i])
        if numero == 0:
            numpar += 1
        elif numero % 2 == 0:
            numpar += 1
        else:
            numimp += 1
        if numero < 0:
            numneg += 1
        else:
            if numero != 0:
                numpos += 1
    result.append(numpos)
    result.append(numneg)
    result.append(numpar)
    result.append(numimp)
    return result

if __name__ == "__main__":
    a = [51,-12,-3,0,2]
    print(clasificar_num(a))
