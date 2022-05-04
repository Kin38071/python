import sqlite3
conn = sqlite3.connect('lididb.sqlite3', isolation_level=None)

cursor = conn.cursor()

#cursor.execute('select id, jmeno, zamestnani from osoba')

#tabulka=cursor.fetchall()

#for radek in tabulka:
#   print(radek)

data = 1990

cursor.execute(f"select id, jmeno, zamestnani from osoba where rok_narozeni > {data}")

for id, jmeno, zamestnani in cursor.fetchall():
    print(id, jmeno, zamestnani)