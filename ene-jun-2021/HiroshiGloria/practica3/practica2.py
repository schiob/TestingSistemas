def triangulos(l):
    if ((l[0]<l[1]+l[2] and l[1]<l[0]+l[2] and l[2]<l[0]+l[1])) and (l[0]!=0 and l[1]!=0 and l[2]!=0):
    	if (l[0]==l[1] and l[1]==l[2]):
    		return "Es equilatero."
    	elif (l[0]==l[1] or l[0]==l[2] or l[1]==l[2]):
    		return "Es isoceles."
    	elif (l[0]!=l[1] or l[0]!=l[2] or l[1]!=l[2]):
    		return "Es escaleno."
    else:
    	return "No se puede construír."
"""        
l = [1,1,2]
print(triangulos(l))
l = [3,3,3]
print(triangulos(l))
l = [1,3,3]
print(triangulos(l))
l = [2,3,4]
print(triangulos(l))
l = [0,3,2]
print(triangulos(l))
"""