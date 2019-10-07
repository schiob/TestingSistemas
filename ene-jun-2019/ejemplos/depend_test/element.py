class Element():
    def __init__(self, name, symbol, at_num, at_mass, family):
        self.name = name
        self.symbol = symbol
        self.atomic_number = at_num
        self.atomic_mass = at_mass
        self.family = family
    
    def __str__(self):
        return "{} - {}".format(self.symbol, self.name)