import time
import datetime

def hora(am, min):

    pm = am + 12

	t2 = datetime.time(pm, min)

    return t2

if __name__ == '__main__':

    nums = list(map(int, input('Que hora quieres cambiar?: ').split(":")))
    res=hora(am, min)

    print("{}")
