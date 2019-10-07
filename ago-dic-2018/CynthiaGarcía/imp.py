
#a=int(input())
#b=int(input())
#nums=list(map(int, input().split()))
#a=nums.pop()
#b=nums.pop()

#print(a)
#print(b)

def NumImpares(a,b):
	suma=0
	for i in range(a+1 , b):
		if i%2 !=0:
			suma=suma+i	
	return suma	

if __name__ == '__main__':
	resultado=Impares(suma)

#print(suma)

	