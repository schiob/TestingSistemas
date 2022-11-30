x = input()
nums = list(map(int, input().split(' ')))

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

print(f"{pos} numero(s) positivo(s)\n{neg} numero(s) negativo(s)\n{par} numero(s) par(es)\n{impar} numero(s) impar(es)")
