
def numbers():
    L = list(map(int, input().split())) 

    list1 = [n for n in L if n > 0]
    print(len(list1), "números positivos")
    list1 = [n for n in L if n < 0]
    print(len(list1), "números negativos")

    list1 = [n for n in L if n % 2 == 0]
    cont = len(list1)
    print(cont, "números pares")
    print(len(L) - cont, "números impares")

numbers()
    
 