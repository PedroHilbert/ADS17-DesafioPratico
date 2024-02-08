import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='controleprojetos',
)

nomeprojeto = input('Qual o nome do projeto que deseja cadastrar? ')
localizacao = input('Qual o endereço do seu projeto? ')
escopo = input('Endereço do escopo: ')
cliente = input('Nome do Cliente: ')
dataInicioPrevista = input('Data de inicio da obra? ')

