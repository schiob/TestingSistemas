#num=int(input("Que cantidad deseas?"))

def ContadorLeds (num):
	contador=0
	list=[]
	aux=0
	num=str(num)
	
	while aux < len(num):
		list.append(num[aux])
		aux+=1  

	for aux in list:
		if aux == '1':
			contador+=2
		if aux =='4':
			contador+=4	
		if aux == '7':
			contador+=3
		if aux == '8':
			contador+=7		
		if aux =='6' or aux =='9' or aux =='0':
			contador+=6	
		if aux == '2' or aux=='3' or aux =='5': 
			contador+=5
	print(contador)
	return contador

if __name__=='__main__':
	resultado=ContadorLeds(num)		
	