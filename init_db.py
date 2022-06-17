import sqlite3

connection = sqlite3.connect('melhorrota.db')

def create_tables():
    with open('melhorrota.sql') as f:
        connection.executescript(f.read())
    return True
