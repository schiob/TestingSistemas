#P6 CyPdS: Funciones

class Funciones_Viajes:
    
    def __init__(self):
        self.users=[]
        self.flag_first_run=0
    
    def siguiente_usuario (self):
        if not self.users and self.flag_first_run==0:
            self.flag_first_run=1
            lines=open("Usuarios.txt","r").readlines()
            for i in lines:
                x=i.split(' ')
                x[1]=int(x[1])
                self.users.append(x)
            self.users=sorted(self.users, key=lambda x: x[1])
        elif not self.users and self.flag_first_run==1:
            return "No hay mas usuarios"
        return self.users.pop(0)[0]

    def extraer_conductores(self):
        conductores=[]
        lines=open("Conductores.txt","r").readlines()
        for i in lines:
            x=i.split(' ')
            x[1]=int(x[1])
            conductores.append(x)
        return conductores
    
    def calcular_tarifa(self,anti):
        return 20+(10*anti)

    def viajes_disponibles(self):
        Cond=self.extraer_conductores()
        Viaj=[]
        i=0
        for i in range(len(Cond)):
            aux=[i+1, int(self.calcular_tarifa(Cond[i][1]))]
            Viaj.append(aux)
        return Viaj
    
    def Main(self):
        UsuVia=""
        Viaj=self.viajes_disponibles()
        Viaj=sorted(Viaj, key=lambda x: x[1])
        Usu=""
        while True:
            Usu=self.siguiente_usuario()
            if not Viaj or Usu=="No hay mas usuarios":
                break
            else:
                aux=str(Usu)+" - viaje "+str(Viaj.pop(0)[1])+"\n"
                UsuVia+=aux
        
        print(UsuVia)
        
viajes=Funciones_Viajes()
#print(viajes.siguiente_usuario())
#print(viajes.extraer_conductores())
#print(viajes.calcular_tarifa(2))
#print(viajes.viajes_disponibles())
viajes.Main()