import mysql.connector

#AQUI VOU USAR O MORKBENCH, ENTÃO tÔ CONECTANDO COM O BANCO DE DADOS QUE CRIEI LÁ. 
conexao = mysql.connector.connect(
    host='localhost',
    user='root', 
    password='123456',
    database='controleprojetos',
)

cursor = conexao.cursor()
'''
nomeprojeto = input('Qual o nome do projeto que deseja cadastrar? ')
localizacao = input('Qual o endereço do seu projeto? ')
escopo = input('Endereço do escopo: ')
cliente = input('Nome do Cliente: ')
dataInicioPrevista = input('Data de inicio da obra? ')
'''
# PARA RODAR O CÓDIGO, DEVE ESCOLHER O BLOCO DE CÓDIGO E RODA-LÓ

#Aqui iremos adicionar um projeto no nosso banco de dados
'''
comando = f'INSERT INTO projetos (nome_projeto, localizacao, escopo, cliente, data_inicio) VALUES ("{nomeprojeto}", "{localizacao}", "{escopo}","{cliente}","{dataInicioPrevista}")'
cursor.execute(comando)
conexao.commit()
'''
#Aqui em baixo estaremos pesquisando os projetos cadastrado
comando = f'SELECT * FROM projetos'
cursor = conexao.cursor()
cursor.execute(comando)

resultado = cursor.fetchall() # ler o banco de dados
print(resultado)























cursor.close()
conexao.close()