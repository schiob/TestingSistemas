n = input('Dame 5 numeros separados por un espaxio -> ')
n = n.split(" ")
if len(n) > 5:
    print('Te dije que solo queria 5 por que con mas no puedo toy chikito :v')
    exit()
else:
    pos = 0
    neg = 0
    par = 0
    impar = 0
    nuetro = 0

    for i in n:
        if int(i) > 0:
            pos += 1

        if int(i) < 0:
            neg += 1

        if int(i) == 0:
            nuetro += 1

        if (int(i) % 2) == 0:
            par += 1
        else:
            impar += 1

    print(f'{pos} número(s) positivo(s)\n'
          f'{neg} número(s) negativo(s)\n'
          f'{nuetro} número(s) neutro(s)\n'
          f'{par} número(s) par(es)\n'
          f'{impar} números impar(es)')