import sqlite3  

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#  leitura dos dados 
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall()) # exibe todos os dados






