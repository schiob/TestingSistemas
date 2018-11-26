import sqlite3
import os
def main():
    conn = sqlite3.connect("social_data.db")
    cur = conn.cursor()
    if not os.path.isfile("social_data.db"):
        conn = sqlite3.connect("social_data.db")
    else:
        pass
    cur.execute('''CREATE TABLE IF NOT EXISTS tabla
        (ID Text,
        Nombre Text,
        Lugar Text,
        Verificado Text,
        Followers Integer,
        Tweets y Retweets Integer,
        Following Integer,
        Descipcion Text,
        Lenguaje Text,
        Foto Text,
        Ranking Text,
        Categoria Text,
        Victorias Integer,
        Derrotas Integer)
        ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
