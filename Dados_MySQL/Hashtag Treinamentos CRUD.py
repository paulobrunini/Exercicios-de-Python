import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql@23',
    database='bdhashtag'
)
cursor = conexao.cursor()

#CRUD
#CREATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO Vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit()  # edita o banco de dados

#READ
# comando = f'SELECT * FROM Vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()  # ler o banco de dados
# print(resultado)

#UPDATE
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE Vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

#DELETE
nome_produto = "todynho"
valor = 6
comando = f'DELETE FROM Vendas WHERE nome_produto = "todynho"'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()