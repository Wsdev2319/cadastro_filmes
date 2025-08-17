import sqlite3 

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()


# excluir dados
id = (1,2)
cursor.execute("""
               
               DELETE FROM filmes WHERE ID in (?,?)
               """, id
            )

conexao.commit()

print('Registro Excluido')