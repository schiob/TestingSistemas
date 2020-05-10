import Volumen
import Contenedor
import math

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
        

        orden = [caja1,caja2,caja3]
        volumenes.sort(reverse=True) ##Ordenamos de manera mayor a menor para hacer las divisiones y verificar el residuo
        orden.sort(reverse=True)
        #print(orden)
        #print(orden)
        #print(volumenes)
        #print(volumenes[0])

        
        result = []
        for n,i in enumerate(orden):
        
            if(i==orden[len(orden)-1]):
                tot = math.ceil(vol/volumenes[n])
                    
            elif(volumenes[n] >= vol):
                result.append(f"(1,{i})")
                    
                return result
            else:
                tot = math.floor(vol/volumenes[n])
                vol %= volumenes[n]
                
            result.append(f"({tot},{i})")   
        return result



if __name__ == "__main__":
    
    c1 = int(input("Escriba el lado de la caja 1:"))
    c2 = int(input("Escriba el lado de la caja 2:"))
    c3 = int(input("Escriba el lado de la caja 3:"))
    v = int(input("Escriba el volumen a almacenar:"))
    
    print(allinone.calnecesario(c1,c2,c3,v))

