import math

def get_content(path):
	try:
		f = open(path)
		content = f.read()
		f.close()

		data = [m.split() for m in content.splitlines()]

		return [{
			"name": d[0],
			"assign": d[1],
			"calif": int(float(d[2]) * 100) / 100.0
		} for d in data]

	except Exception:
		return []

def get_average(content):
	students = list(dict.fromkeys([k["name"] for k in content]))
	matters_by_student = [{"name": st, "mtt": list(filter(lambda co: co["name"] == st, content))} for st in students]
	average = [{"name": s["name"], "avg": sum([m["calif"] for m in s["mtt"]]) / len(s["mtt"])} for s in matters_by_student]

	return "\n".join(["{name} {avg:.2f}".format(name = av["name"], avg = av["avg"]) for av in average])

def read_and_get_average(path):
	return get_average(get_content(path))

if __name__ == "__main__":
	print(read_and_get_average("perro.txt"))