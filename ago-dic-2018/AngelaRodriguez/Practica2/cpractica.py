#n= int(input())
#nums=list (map (int, input().split(" ")))

def calc(numbers):
	par = impar = pos = neg = 0

	for num in numbers:
		if num%2==0:
			par+=1
		else:
			impar+=1
		if num<0:
			neg+=1
		elif num>0:
			pos+=1
	return par, impar, neg, pos

if __name__ == '__main__':

	n=int(input())
	nums=list(map (int, input().split(" ")))

	resultado=calc(nums)

	print("Pares = {}".format(resultado[0]))
	print("Impar = {}".format(resultado[1]))
	print("Negativo = {}".format(resultado[2]))
	print("Positivo = {}".format(resultado[3]))


