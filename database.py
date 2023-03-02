import sqlite3 

conn = sqlite3.connect('users.db')

cursor = conn.cursor()

cursor.execute( '''
CREATE TABLE IF NOT EXISTS User (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXTO NOT NULL,
    Senha TEXT NOT NULL,
    Confsenha TEXT NOT NULL


)
''')

print("conexao sim")