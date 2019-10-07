var = input("dame la hora: ")

if var.find("p.m") != -1:
	ent = int(var[:2])
	ent = ent + 12
	nel = str(ent) + var[2:5] + "hrs"
	print(nel)
else:
	print(var[:5] + "hrs")
