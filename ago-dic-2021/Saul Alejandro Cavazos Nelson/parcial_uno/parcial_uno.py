def parcial_uno(entrada):
    guiso=str(entrada).split()
    n=len(guiso)
    precio=0
    if n<=30:
        for i in range (0,n,1) :
            if guiso[i] == 'cachete':
                precio+=13
            elif guiso[i] == 'lengua':
                precio+=10
            elif guiso[i] == 'tripitas':
                precio+=9
            elif guiso[i] == 'pastor':
                precio+=15
            elif guiso[i] == 'machito':
                precio+=14
    return precio
if __name__ =='__main__':
    entrada=input()
    print(parcial_uno(entrada))