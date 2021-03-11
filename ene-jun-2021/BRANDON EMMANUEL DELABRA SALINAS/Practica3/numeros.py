
def Check_Num(numeros):

    negative = 0
    positive = 0
    par = 0 
    impar = 0
    ceros = 0

    for i in numeros:

        if i < 0:
            negative += 1

        if i > 0:
            positive += 1      

        if (i) % (2) == 0:
            par += 1   

        if (i) % (2) != 0:
            impar += 1  
          
        if i == 0:
            ceros += 1 

    return (f'{negative} número(s) negativo(s)\n'
            f'{positive} número(s) positivo(s)\n'
            f'{par} número(s) par(es)\n'
            f'{impar} número(s) impa(es)\n'
            f'{ceros} número(s) neutro(s)')

if __name__ == "__main__":

    num = input('Ingresa 5 números').split()
    numeros = list(map(int, num))
    print (numeros)
    print(Check_Num(numeros))

   