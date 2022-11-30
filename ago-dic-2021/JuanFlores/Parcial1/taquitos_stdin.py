tacos = input().split(' ')

menu = {
    'cachete': 13,
    'lengua': 10,
    'tripitas': 9,
    'pastor': 15,
    'machito': 14,
}

total = 0
for t in tacos:
    total += menu[t]

print(total)