def bonAppetit(n, k, b, ar):
    charge = 0
    for val in ar:
        charge += val/2.0
    charge = charge - ar[k]/2.0
    if b == charge:
        return 'Bon Appetit'
    else:
        return int(b-charge)
    

def main():
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    ar = list(map(int, input().strip().split(' ')))
    b = int(input().strip())
    result = bonAppetit(n, k, b, ar)
    print(result)

if __name__ == "__main__": 
    main()    