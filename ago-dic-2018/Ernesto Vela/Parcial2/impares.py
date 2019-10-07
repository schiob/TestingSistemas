def imp(nums):
    total = 0
    nums.sort()
    for i in range(nums[0],nums[1]):
        if int(i) % 2 != 0:
            if i > nums[0] and i < nums[1]:
                 total += int(i)

    return total

if __name__ == '__main__':

    nums = list(map(int, input('Escribe los extremos del rango separados por un espacio: ').split(" ")))
    res=imp(nums)

    print("La suma de los valores impares es: {}".format(res))
