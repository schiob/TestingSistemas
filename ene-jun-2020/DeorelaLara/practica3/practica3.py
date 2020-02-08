listx = [1, 1, 2, 2, -1, -1, -2, -2]
listy = [2, -2, 1, -1, 2, -2, 1, -1]
print(listx)
print(listy)

def valor(nx, ny):
    if(nx >= 0 and nx < 8 and ny >= 0 and ny <8):
        print('ok')
    else:
        print('not ok')

print(valor(7,7))