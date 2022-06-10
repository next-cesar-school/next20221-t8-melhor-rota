import sqlite3

connection = sqlite3.connect('melhorrota.db')

with open('melhorrota.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO caminhoes (descricao, localizacao, status) VALUES (?, ?, ?)", ('caminhao A', 'INT8', True))

cur.execute("INSERT INTO caminhoes (descricao, localizacao, status) VALUES (?, ?, ?)", ('caminhao B', 'INT6', False))


connection.commit()
connection.close()