def tri_from_file(name:str)->str:
    f=open(name)
    num=f.read()
    tu,td,tt = num.split()
    sumuno=int(tu)+int(td)
    sumdos=int(tu)+int(tt)
    sumtres=int(td)+int(tt)
    tu=int(tu)
    tt=int(tt)
    td=int(td)
    if tu>0 and tu==td and tu==tt:
        return 'Equilátero'
    elif tu==td and tu!=tt:
        return 'Isóceles'
    elif td==tt and td!=tu:
        return 'Isóceles'
    elif tt==tu and tt!=td:
        return 'Isóceles'
    elif sumuno<=tt or sumdos<=td or sumtres<=tu:
        return 'No triángulo'
    elif tu==0 or td==0 or tt==0:
        return 'No triángulo'
    elif tu!=td and tu!=tt and tt!=td:
        return 'Escaleno'

if __name__ == "__main__":
    print(tri_from_file('testUno.txt'))