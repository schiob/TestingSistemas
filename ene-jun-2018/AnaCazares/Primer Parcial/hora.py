def time_convertion(horas):
    #espacios 00:00:00
    hr=int(hora[0:2])
    min=(hora[3:5])
    seg=(hora[6:8])

    if hora[8:10]=="am" or hora[8:10]=="AM":    
        if hr==12:
            hr="00"
    elif hora[8:10]=="pm" or hora[8:10]=="PM":
        if hr>=1 and hr<=11:
            hr+=12

    hora24= str(hr) + ":" + str(min) + ":" + str(seg)
    return hora24

if __name__ == '__main__':
    hora=input("hora (hh:mm:ssAM/PM): ")
    result = time_convertion(hora)
    print(result)
