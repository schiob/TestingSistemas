def n_triangular(n):
    r = (n * (n + 1)) // 2
    return r


def main():
    n = int(input('Dime el numero al que le quierese sacar el triangular prrio -> '))
    print(n_triangular(n))


if __name__ == '__main__':
    main()
