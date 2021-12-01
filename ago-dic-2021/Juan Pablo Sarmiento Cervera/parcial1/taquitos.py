def orden(Taquitos):
#Orden = input("Dime cuales ordenes de tacos quieres: ").split(',')
#suma = int(Orden)
#sum(suma)
    total = 0
    ordTaquitus = Taquitos.split(',')
    if 0 <len(ordTaquitus)<=30 :
        for ordu in ordTaquitus:
             if ordu == 'cachete': 
                total= total + 13
             elif ordu=='lengua':
                total= total + 10
             elif ordu =='tripas':
                 total=total + 9
             elif ordu =='pastor':
                 total=total + 15
             elif ordu =='machito':
                 total=total + 14
             else:
                 print('lo siento wero de ese"{ordu}"No tengo')
                 total=total
        return('En total serian:\n ${total}')      
            # total =0
    else:
        print("solo se pueden pedir de 1 hasta 30 ordenes de taquitus")

if __name__ == '__main__':
    ordenTacos = input('¿De que va a querer joven?')
    print(orden(ordenTacos))
#for i in 0 < Orden <=30:    
    #if 0 < Orden <=30:
#     print(Orden)
#     print("Solo puedes ordenar de 1 a 30 Ordenes")
#print(Orden)
#print(suma)