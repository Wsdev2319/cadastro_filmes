import sqlite3 

# conectar no Bd

def conecta_db():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# Inserir dados

def inserir_dados(nome, ano , nota):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute('''
                   INSERT INTO filmes(nome, ano, nota)
                   VALUES (?,?,?)
                   ''', (nome, ano, nota)
                )
    conexao.commit()
    conexao.close()
    
# Listagem de Dados
def obter_dados():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close()
    return dados 
    
    