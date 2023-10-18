import mysql.connector
from desafio import (atualizar_produto, deletar_produto, inserir_produtos, selecionar_produto)


conexao = mysql.connector.connect(
host= 'localhost',
user='root',
password = '12345678',
database = 'bd_crud'
)
cursor = conexao.cursor()


# CREATE
inserir_produtos()


# READ
# selecionar_produto()


# UPDATE
# atualizar_produto()

# DELETE
# deletar_produto()



cursor.close()
conexao.close()