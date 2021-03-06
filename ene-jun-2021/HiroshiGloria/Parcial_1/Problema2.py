def get_Contenido(path):
	try:
		archivo = open(path)
		contenido = archivo.read()
		archivo.close()
		return contenido
	except OSError:
		return ""

def convertir_contenido(info):
	# try to parse the info
	try:
		datos = [mix.split(",") for mix in info.splitlines() ]
	except Exception:
		return []

	if(len(datos) > 0):
		headers = datos[0]
		nheaders = len(headers)

		table = []
		for i in range(1, len(datos)):
			ran = datos[i]
			table_it = {}

			if len(ran) == nheaders:
				for j in range(nheaders):
					table_it[headers[j].strip()] = ran[j].strip()
			else:
				return []

			table.append(table_it)

		return table

	return []

def parse_Contenido_C(datos):
	# checks the general headers
	if len(datos) > 0 and not ("usuario" in datos[0] and "correo" in datos[0] and "puntos" in datos[0]):
		return []

	try:
		nuevo_dat = [m for m in datos]

		for n in nuevo_dat:
			if not "@" in n["correo"]:
				return []

			n["puntos"] = float(n["puntos"])

		return nuevo_dat
	except Exception:
		return []

def get_Promedio(datos):
	def get_puntos_x_dom(datos, dom):
		return [o["puntos"] for o in datos if o["correo"].split("@")[1] == dom]

	def get_Prom_puntos(lpuntos):
		return sum(lpuntos) / len(lpuntos)

	def get_all_doms(datos):
		nlista = []

		for m in datos:
			dom = m["correo"].split("@")[1]

			if not dom in nlista:
				nlista.append(dom)

		return nlista

	return [{
		"domain": dom,
		"average": get_Prom_puntos(get_puntos_x_dom(datos, dom))
	} for dom in get_all_doms(datos)]



if __name__ == "__main__":
	content = get_Contenido("users.csv")
	newcontent = convertir_contenido(content)
	parsed_content = parse_Contenido_C(newcontent)
	average = get_Promedio(parsed_content)

	# print the results
	for a in average:
		print(f"{a['domain']} {a['average']}") 