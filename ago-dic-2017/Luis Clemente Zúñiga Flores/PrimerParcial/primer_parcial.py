def Tri_from_file(ruta):

    lista = []
    with open(ruta,'r') as f:
        a = f.read().split()      
    for i in a:
        try:
            lado = float(i)
            lista.append(lado)
        except Exception as inst:
            pass    
    if len(lista)!=3:
        return 'No triángulo'
    else:
        a = lista[0]
        b = lista[1]
        c = lista[2]
    #return lista

    
    #Casos no triángulo
    for i in lista:        
        if i < 1:
            return 'No triángulo'
            break       
    
    if a + b <= c:
        return 'No triángulo'
    
    elif a + c <= b:
        return 'No triángulo'
    
    elif c + b <= a:
        return 'No triángulo'

   #Casos equilatero
    
    elif a == b == c:
        return 'Equilátero'
    #Casos isósceles
    
    elif a == b or a == c:
        return 'Isósceles'
    
    elif b == c or b == a:
        return 'Isósceles'
    
    elif c == a or c == b:
        return 'Isósceles'
    
    elif a!= b !=c:
        return 'Escaleno'
    
#print(Tri_from_file('tri.txt'))


