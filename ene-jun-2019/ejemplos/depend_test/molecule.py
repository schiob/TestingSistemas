from element import Element

class Molecule():
    def __init__(self, name, *elements):
        self.name = name
        self.elements = elements
    
    def __str__(self):
        s = "----{}----".format(self.name)
        for e in self.elements:
            s += "\n"+str(e)
        return s

if __name__ == "__main__":
    e = Element("Hidrógeno", "H", 1, 1, "1")
    c = Element("Carbono", "C", 6, 6, "23")

    m = Molecule("Metal", c, e)
    for elem in m.elements:
        print(elem)

