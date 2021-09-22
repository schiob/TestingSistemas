linea = input()

#logica

cont = 0
for letra in linea:
    if letra in "aeiou":
        cont += 1

print(cont)