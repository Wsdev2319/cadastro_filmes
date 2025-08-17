import sqlite3 

conexao = sqlite3.connect('titulo.db')

# Criando o cursor
cursor = conexao.cursor()

# criando a tabela
cursor.execute("""
               CREATE TABLE filmes(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   ano INTEGER NOT NULL,
                   nota REAL NOT NULL
                   );"""
                )

conexao.close()
print("Criado com sucesso!")

