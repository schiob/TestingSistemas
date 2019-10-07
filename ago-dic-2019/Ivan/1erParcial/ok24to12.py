"""
Primer parcial
EL programa tiene que tener una funcion que tome un string
representando la hora en formato 24 horas: HH:MMhrs y
regrese un string con el formato de un reloj de 24

regn Ivan Medina Martinez
2-10-19
"""


def timestr(hora):
	
	if ((0<=int(hora[0]+hora[1])<24)and(0<=int(hora[3]+hora[4])<60)):
		h=""
		m=""
		if(int(str(hora[0]+hora[1]))>=12):
		    time="p.m."
		elif (int(hora[0]+hora[1])<12):
		    time="a.m."


		if ((hora[0] and hora[1])=="0"):
		    h="12"
		    time="a.m."
		elif((hora[0] + hora[1]) ==12):
		    h="12"
		    time="a.m."
		if (int(hora[0]+hora[1])>12):
		    h=str(int(hora[0]+hora[1])-12)
		    if len(h)==1:
		    	h="0"+h
		else:
			h=str((hora[0]+hora[1]))
			if len(h)==1:
				h="0"+h
		m=hora[3]+hora[4]

		return "{}:{}{}".format(h,m,time)


if __name__ == '__main__':
		

	hora="14:23hrs"
	timestr(hora)