def is_positive(number):
    if number > 0:
        return True
    else:
        return False

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def numbers_summary(numbers):
    positive, negative, even, odd = 0, 0, 0, 0
    for number in numbers:
        number = int(number)
        if number != 0:
            if is_positive(number) and is_even(number):
                positive += 1
                even += 1
        
            elif not is_positive(number) and is_even(number):
                negative += 1
                even += 1
            
            elif is_positive(number) and not is_even(number):
                positive += 1
                odd += 1
            
            else:
                negative += 1
                odd += 1
        else:
            even += 1
    return "{} número(s) positivo(s)\n{} número(s) negativo(s)\n{} número(s) par(es)\n{} número(s) impar(es)".format(positive, negative, even, odd)

def main():
    n = int(input())
    line = input().split(" ")
    if 0 < len(line) <= n:
        print(numbers_summary(line))
    
if __name__ == '__main__':
    main()