
def triangle_from_file(path):
	try:
		# Read the file
		f = open(path)
		content = f.read()
		f.close()

		# Process the content
		triangle = [float(m) for m in content.split()]

		# Check if is a triangle
		if len(triangle) != 3 or len([m for m in triangle if sum(triangle) - m <= m]) > 0:
			return "No triangulo"

		# Return the triangle type
		if sum(triangle) == triangle[0] * 3:
			return "Equilatero"

		if triangle[0] in triangle[1:] or triangle[1] == triangle[2]:
			return "Isoceles"

		return "Escaleno"

	except Exception:
		return "No triangulo"
