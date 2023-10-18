import mysql.connector


conexao = mysql.connector.connect(
host= 'localhost',
user='root',
password = '12345678',
database = 'bd_crud'
)


def inserir_produtos():
    cursor = conexao.cursor()
    qnt_prod = int(input("Quantos produtos são? "))
    for i in range(qnt_prod):
        produto = input('Digite seu produto: ')
        valor = float(input('Digite o valor: '))
        comando = f"INSERT INTO vendas(produto, valor) values('{produto}', {valor})"
        cursor.execute(comando)
        conexao.commit()

    
    return 'Confira o Banco'

def selecionar_produto():
    cursor = conexao.cursor()
    comando = 'select * from vendas'
    cursor.execute(comando)
    leitura = cursor.fetchall()
    print(leitura)

    return 'Veja'


def atualizar_produto():
    cursor = conexao.cursor()
    valor = float(input('Digite o valor: '))
    id = int(input("Digite o ID: "))
    comando = f'UPDATE vendas SET valor = {valor} WHERE id = {id}'
    cursor.execute(comando)
    conexao.commit()
    return 'Olha la'

def deletar_produto():
    cursor = conexao.cursor()
    id = int(input("Digite o ID: "))
    comando = f'DELETE FROM vendas WHERE id = {id}'
    cursor.execute(comando)
    conexao.commit()
    return 'Olha lá'


