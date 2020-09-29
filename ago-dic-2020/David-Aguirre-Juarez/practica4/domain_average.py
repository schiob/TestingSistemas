
# LA SOLUCIÓN A ESTE PROBLEMA ES REALMENTE MALO Y REQUIERE DE REFACTORIZACIÓN.
# SE CODIFICARON PRIMERO LAS PRUEBAS ANTES DE LA SOLUCIÓN.

def get_content_file(path):
	try:
		f = open(path)

		content = f.read()
		f.close()

		return content
	except OSError:
		return ""

def convert_content(info):
	# try to parse the info
	try:
		data = [m.split(",") for m in info.splitlines() ]
	except Exception:
		return []

	if(len(data) > 0):
		headers = data[0]
		nheaders = len(headers)

		table = []
		for i in range(1, len(data)):
			r = data[i]
			table_it = {}

			if len(r) == nheaders:
				for j in range(nheaders):
					table_it[headers[j].strip()] = r[j].strip()
			else:
				return []

			table.append(table_it)
		
		return table

	return []

def parse_converted_content(data):
	# checks the general headers
	if len(data) > 0 and not ("usuario" in data[0] and "correo" in data[0] and "puntos" in data[0]):
		return []

	try:
		new_data = [m for m in data]

		for n in new_data:
			if not "@" in n["correo"]:
				return []

			n["puntos"] = float(n["puntos"])

		return new_data
	except Exception:
		return []

def get_average(data):
	def get_points_by_domain(data, domain):
		return [o["puntos"] for o in data if o["correo"].split("@")[1] == domain]

	def get_average_of_points(lpoints):
		return sum(lpoints) / len(lpoints)

	def get_all_domains(data):
		nlist = []

		for m in data:
			dom = m["correo"].split("@")[1]

			if not dom in nlist:
				nlist.append(dom)

		return nlist

	return [{
		"domain": dom,
		"average": get_average_of_points(get_points_by_domain(data, dom))
	} for dom in get_all_domains(data)]



if __name__ == "__main__":
	content = get_content_file("users.csv")
	newcontent = convert_content(content)
	parsed_content = parse_converted_content(newcontent)
	average = get_average(parsed_content)

	# print the results
	for a in average:
		print(f"{a['domain']} {a['average']}")