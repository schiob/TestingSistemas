class Card:
    def __init__(self, id, name, types, desc, price):

        self._Id = id
        self._Name = name
        self._Type = types
        self._Desc = desc
        #self.Atk = atk
        #self.Def = defs
        #self.Level = level
        #self.Race = race
        #self.Attribute = attribute
        self._Price = price


    def __str__(self):
        return """
        Id: {}
        Name: {}
        Type: {}
        Desc: {}
        Price: {}
    
        """.format(self._Id, self._Name, self._Type, self._Desc, self._Price)
