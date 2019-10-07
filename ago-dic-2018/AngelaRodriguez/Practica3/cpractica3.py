def triangulo(num):

	
		trian= (num*(num+1))/2


		return trian

if __name__ == '__main__':

	num=int(input())
	

	resultado=triangulo(num)

	print('<', num,',', resultado, '>')
