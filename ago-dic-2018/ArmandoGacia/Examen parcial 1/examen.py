def hora(string):
    if n[0] == "0":
        if n[1] == "1":
            if n[5] == "a":
                print("01:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("13:{}{}hrs".format(n[3],n[4
        elif n[1] == "2":
            if n[5] == "a":
                print("02:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("14:{}{}hrs".format(n[3],n[4]))
        elif n[1] == "3":
            if n[5] == "a":
                print("03:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("15:{}{}hrs".format(n[3],n[4]))
        elif n[1] == "4":
            if n[5] == "a":
                print("04:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("16:{}{}hrs".format(n[3],n[4]))
        elif n[1] == "5":
            if n[5] == "a":
                print("05:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("17:{}{}hrs".format(n[3],n[4]))
        elif n[1] == "6":
            if n[5] == "a":
                print("06:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("18:{}{}hrs".format(n[3],n[4]))
        elif n[1] == "7":
            if n[5] == "a":
                print("07:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("19:{}{}hrs".format(n[3],n[4]))
        elif n[1] == "8":
            if n[5] == "a":
                print("08:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("20:{}{}hrs".format(n[3],n[4]))
        elif n[1] == "9":
            if n[5] == "a":
                print("09:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("21:{}{}hrs".format(n[3],n[4]))
    if n[0] == "1":
        if n[1] == "0":
            if n[5] == "a":
                print("10:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("22:{}{}hrs".format(n[3],n[4]))
        elif n[1] == "1":
            if n[5] == "a":
                print("11:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("23:{}{}hrs".format(n[3],n[4]))
        elif n[1] == "2":
            if n[5] == "a":
                print("00:{}{}hrs".format(n[3],n[4]))
            elif n[5] == "p":
                print("12:{}{}hrs".format(n[3],n[4]))


if __name__ == '__main__':
    n=input('Dame la hora')
    hora(n)
