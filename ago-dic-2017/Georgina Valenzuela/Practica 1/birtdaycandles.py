import sys

def birthdayCandles(n, height):
    counter= 0
    maxheight = max(height)
    

    for h in height:
        if maxheight == h:
                counter= counter+1
        else:
            break
        return counter

if __name__ == "__main__":  
        n= int(input().strip())
        height=list(map(int, input().strip().split(' ')))

        result= birthdayCandles(n,height)
        print (result)
