import sqlite3

# conectando db 
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# Inserindo dados 
cursor.execute("""
               
               INSERT INTO filmes(nome, ano, nota)
               VALUES ('Sonic', 2023, 7.0)
               
               """)

conexao.commit() # Salva as alteraçoes
conexao.close()
print("Dados inserido com sucesso!")

