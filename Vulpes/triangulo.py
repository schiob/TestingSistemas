nums = input("Inserta tres números (: \n")
a,b,c = nums.split(" ")
num1 = int(a)
num2 = int(b)
num3 = int(c)

#Para saber si se puede crear un triángulo
if (num1+num2>num3 and num1+num3>num2 and num2+num3>num1):
#Saber qué tipo de triángulo es
	if (num1==num2 and num1==num3):
		print("Es un triángulo equilátero")
	elif (num1==num2 or num2==num3 or num1==num3):
		print("Es un triángulo isóceles")
	else:
		print("Es un triángulo escaleno")
else:
	print("Los números ",num1,", ",num2," y ",num3," NO forman un triángulo")
