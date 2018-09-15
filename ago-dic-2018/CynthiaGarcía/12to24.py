from datetime import time

time="1:00 pm"
#time=time.pop()
def conversion (time):

	date_obj=time.strp(time, '%I,%M%p')

	if time<=12:
		hora=time-12
	print (hora+'hrs')
	else
		print(time+'hrs')

if __name__== '__main__'
	
	


