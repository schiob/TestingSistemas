
def calc(nums): #creando una funcion
	impar=0
	neg=0
	pos=0
	par=0
	for i in nums:
		if i %2==0:
			par += 1
		else: impar += 1

		if i<0:
			neg+=1
		elif i>0:
			pos+=1
	return par, impar, pos, neg

if __name__ == '__main__':
	n=int(input())
	nums=list(map(int, input().split(" ")))  #map--- aplica la conversion a a todos los elementos que le siguen 

	resultado=calc(nums)
	print ("pares = {} ".format(0))
	print ("impares = {}".format(1))
	print ("pos = {}".format(2))
	print ("neg = {}".format(3))


