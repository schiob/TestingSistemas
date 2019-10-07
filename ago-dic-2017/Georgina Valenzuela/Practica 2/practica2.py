import sys 

def printFile (path):
	file = open(path)
	return file.read ()

def writeFile (path, string):
	file = open (path,'w')
	file.write(string)

if __name__ == '__main__':
	writeFile("testFile.txt", "Charmander")
	print (printFile("testFile.txt"))