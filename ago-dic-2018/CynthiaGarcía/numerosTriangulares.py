def calcNT(posicion):

	triangular= int(pos*(pos+1)/2)	

	return triangular
if __name__ == '__main__':
	pos=int(input())
	trian=calcNT(pos)

	print ("Triangular={}".format (trian))