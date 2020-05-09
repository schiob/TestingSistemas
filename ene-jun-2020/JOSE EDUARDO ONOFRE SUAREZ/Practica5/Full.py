import Volumen
import Contenedor

class allinone:

    def calnecesario(caja1,caja2,caja3,vol):

        volumenes = []
        isComplete = True
        volacum = 0
        l1 = [1,1,1]
        
        #Calculamos el volumen de la caja segun sus lados
        v1 = Volumen.volumen.calVol(caja1,caja1,caja1)
        volumenes.append(v1)
        v2 = Volumen.volumen.calVol(caja2,caja2,caja2)
        volumenes.append(v2)
        v3 = Volumen.volumen.calVol(caja3,caja3,caja3)
        volumenes.append(v3)

        volacum = Contenedor.contenedor.volumencontenedor(l1,volumenes)

        if volacum<vol:
            dif = vol - volacum
            print("Te faltan {} unidades para completar".format(dif)) 
        

        return 
        




if __name__ == "__main__":
    
    c1 = int(input("Escriba el lado de la caja 1:"))
    c2 = int(input("Escriba el lado de la caja 2:"))
    c3 = int(input("Escriba el lado de la caja 3:"))
    v = int(input("Escriba el volumen a almacenar:"))

    print(allinone.calnecesario(c1,c2,c3,v))

