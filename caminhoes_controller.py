import sqlite3

def get_db_connection():
    conn = sqlite3.connect('melhorrota.db')
    #conn.row_factory = sqlite3.Row
    return conn

# Comandos GET, POST, PUT

def insert_caminhao(descricao, localizacao, status):
    db = get_db_connection()
    cursor = db.cursor()
    statement = "INSERT INTO caminhoes(descricao, localizacao, status) VALUES (?, ?, ?)"
    cursor.execute(statement, [descricao, localizacao, status])
    db.commit()
    return True


def update_caminhao(id, descricao, localizacao, status):
    db = get_db_connection()
    cursor = db.cursor()
#    statement = "UPDATE caminhoes SET descricao = ?, localizacao = ?, status = ? WHERE id = ?"
    statement = "UPDATE caminhoes SET descricao = ?, localizacao = ?, status = ? WHERE id = ?"
    cursor.execute(statement, [descricao, localizacao, status, id])
    db.commit()
    return True


def delete_caminhao(id):
    db = get_db_connection()
    cursor = db.cursor()
    statement = "DELETE FROM caminhoes WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db_connection()
    cursor = db.cursor()
    statement = "SELECT * FROM caminhoes WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_caminhoes():
    db = get_db_connection()
    cursor = db.cursor()
    query = "SELECT * FROM caminhoes"
    cursor.execute(query)
    return cursor.fetchall()
