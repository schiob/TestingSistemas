def triangle(lados):
    cont = 0
    for i in range(len(lados)-1):
        if (lados[i] == lados[i + 1]):
            cont += 1
    if cont == 0:
        print('Escaleno')
    if cont == 1:
        print('Isosceles')
    if cont == 2:
        print('Equilatero')

medidas = input().split(' ')
triangle(medidas)

'''
<(1,2,3),'Escaleno'>
<(2,1,3),'Escaleno'>
<(3,2,1),'Escaleno'>
<(1,1,2),'Isosceles'>
<(1,2,1),'Isosceles'>
<(2,1,1),'Isosceles'>
<(1,1,1),'Equilatero'>
<(0,2,3),'No triangulo'>
<(1,2,0),'No triangulo'>
<(1,0,3),'No triangulo'>
<(0,0,1),'No triangulo'>
<(0,0,0),'No triangulo'>
'''