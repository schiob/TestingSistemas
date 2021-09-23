def tacos(t_tacos):
    #cachete=0
    #lengua=0
    #tripitas=0
    #pastor=0
    #machito=0
    cuenta=0
    for i in t_tacos:
        if i =="cachete":
            cuenta=cuenta+13
        elif i =='lengua':
            cuenta=cuenta+10
        elif i =='tripitas':
            cuenta=cuenta+9
        elif i =='pastor':
            cuenta=cuenta+15
        elif i =='machito':
            cuenta=cuenta+14
   #cuenta=0#cachete+lengua+tripitas+pastor+machito
    if len(t_tacos)<=30:
        return(cuenta)
    else:
        return('orden no debe exeder las 30 unidades')


if __name__=="__main__":
    
    t_tacos=list(input("---\n").split())
    
    print(tacos(t_tacos))
