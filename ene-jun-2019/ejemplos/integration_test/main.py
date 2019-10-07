import sqlite3

class Taco():
    def __init__(self, tortilla, guiso, salsa):
        self.tortilla = tortilla
        self.guiso = guiso
        self.salsa = salsa

    def __str__(self):
        return "Taco de {} con {} y salsa {}".format(self.tortilla, self.guiso, self.salsa)

    def __eq__(self, taco):
        if taco.tortilla != self.tortilla:
            return False

        if taco.guiso != self.guiso:
            return False

        if taco.salsa != self.salsa:
            return False
        return True

class sqlite():
    def __init__(self, archivo):
        self.conn = sqlite3.connect(archivo)

    def save(self, taco):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO TACOS (tortilla, guiso, salsa) VALUES ('{}', '{}', '{}')".format(taco.tortilla, taco.guiso, taco.salsa))

    def getAllTacos(self):
        cur = self.conn.cursor()
        tt = cur.execute("SELECT * FROM TACOS").fetchall()

        tacos = []
        for t in tt:
            tacos.append(Taco(t[1], t[2], t[3]))
        return tacos


def saveTaco(taco, db):
    db.save(taco)

def showTacos(db):
    tacos = db.getAllTacos()
    return tacos

if __name__ == "__main__":
    taquito = Taco("harina", "bistek", "roja")
    taquito2 = Taco("harina", "picadillo", "verde")
    taquito3 = Taco("maiz", "pastor", "chipotle")
    taquito4 = Taco("maiz", "pirata", "habanero")

    db = sqlite("archivito.db")
    # cur = db.conn.cursor()
    # cur.execute("CREATE TABLE TACOS (id INTEGER PRIMARY KEY AUTOINCREMENT,tortilla TEXT, guiso TEXT, salsa TEXT)")


    saveTaco(taquito, db)
    saveTaco(taquito2, db)
    saveTaco(taquito3, db)
    saveTaco(taquito4, db)
    print(*showTacos(db), sep="\n")