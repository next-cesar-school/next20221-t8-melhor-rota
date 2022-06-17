import sqlite3

def get_db_connection():
    conn = sqlite3.connect('melhorrota.db')
    return conn

# Comandos GET, POST, PUT, DELETE, GET ID

def insert_caminhao(descricao, localizacao, status):
    db = get_db_connection()
    cursor = db.cursor()
    statement = "INSERT INTO caminhoes(descricao, localizacao, status) VALUES (?, ?, ?)"
    cursor.execute(statement, [descricao, localizacao, status])
    db.commit()
    return "Inclusão realizada com sucesso."


def update_caminhao(id, descricao, localizacao, status):
    db = get_db_connection()
    cursor = db.cursor()
    statement = "UPDATE caminhoes SET descricao = ?, localizacao = ?, status = ? WHERE id = ?"
    cursor.execute(statement, [descricao, localizacao, status, id])
    db.commit()
    return "Alteração realizada com sucesso"


def delete_caminhao(id):
    db = get_db_connection()
    cursor = db.cursor()
    statement = "DELETE FROM caminhoes WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return "Caminhão Apagado com Sucesso"


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
