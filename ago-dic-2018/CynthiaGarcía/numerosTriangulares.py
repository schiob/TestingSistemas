def calcNT(pos):

	triangular= int(pos*(pos+1)/2)	

	return triangular
if __name__ == '__main__':
	pos=int(input())
	resultado=calcNT(pos)

	print ("Triangular=", resultado)