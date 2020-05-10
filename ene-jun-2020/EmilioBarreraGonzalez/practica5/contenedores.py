import math
#Function to calculate the volume 
#Of a cubic container given it's 
#3 sides
def vol_calc(side1: float, side2: float, side3: float) -> float: 
    try:
       vol = float(side1 * side2 * side3)
       return vol
    except:
        print("Numeric values for each of the 3 sides were expected")
        return -1 #ERROR CODE

def total_vol(containers: list) -> float: 
    rvalue=0
    for i in containers:
        a=i.split(',')
        rvalue+=float(a[0])*float(a[1])
    return rvalue

def saving_strat(side: list,vol: float, volume_calc: object) -> list: 
    rvalue=[]
    side.sort(reverse=True)
    for i in side:
        if(i==side[len(side)-1]):
            tot = math.ceil(vol/volume_calc(i,i,i))
        elif(volume_calc(i,i,i) >= vol):
            rvalue.append(f"({i},1)")
            return rvalue
        else:
            tot = math.floor(vol/volume_calc(i,i,i))
            vol %= volume_calc(i,i,i)
        rvalue.append(f"({i},{tot})")
    return rvalue

if __name__ == '__main__':
    side=[1,2,3]
    print(saving_strat(side, 100, vol_calc))