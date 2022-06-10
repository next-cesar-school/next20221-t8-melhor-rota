import sqlite3

connection = sqlite3.connect('melhorrota.db')

def create_tables():
    with open('melhorrota.sql') as f:
        connection.executescript(f.read())
    return True
#cur = connection.cursor()

#cur.execute("INSERT INTO caminhoes (descricao, localizacao, status) VALUES (?, ?, ?)", ('caminhao A', 'INT8', True))

#cur.execute("INSERT INTO caminhoes (descricao, localizacao, status) VALUES (?, ?, ?)", ('caminhao B', 'INT6', False))

#cur.execute("INSERT INTO caminhoes (descricao, localizacao, status) VALUES (?, ?, ?)", ('caminhao C', 'INT9', True))


#connection.commit()

#connection.close()