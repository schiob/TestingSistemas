regalo = []
precio = []
entrada = input()
regalos=entrada.split(" ")
list(regalos)
# controlRemoto 450.00 hamburguesa 90.00 Switch 6999.99 tarjetaRegalo 500.00 PixelCelular 15000.00
r1 = []
r1 = (regalos[0], regalos[1])
r2 = []
r2 = (regalos[2], regalos[3])
r3 = []
r3 = (regalos[4], regalos[5])
r4 = []
r4 = (regalos[6], regalos[7])
r5 = []
r5 = (regalos[8], regalos[9])

data = [[r1, r2, r3, r4, r5]] 



print(r1,"\n",r2,"\n",r3,"\n",r4,"\n",r5)
print(data)
#print(list(regalos))
