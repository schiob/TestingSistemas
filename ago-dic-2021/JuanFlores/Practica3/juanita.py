
def numeros(x, nums):
    nums = list(map(int, nums.split(' ')))

    pos= neg= par= impar = 0

    for num in nums:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1

    resultado = f"{pos} número(s) positivo(s)\n{neg} número(s) negativo(s)\n{par} número(s) par(es)\n{impar} número(s) impar(es)"
    return resultado