
def clean_file(file):
	new_file=""

	for line in file:
		for character in line:
			if character.isalpha() or unicode(character).isnumeric() or ord(character) == 0x20 or ord(character)==0xa:
				if character.isalpha:
					if ord(character)>=0x41 and ord(character)<=0x5a:
						character=character.lower()
						new_file=new_file+character
					else:
						new_file=new_file+character #si el alpha que revise si es mayus
				else:
					new_file=new_file+character
	#file.close()
	return new_file

if __name__ == '__main__':
	filetext=open('prueba.txt','r')
	a=clean_file(filetext)
	print a
