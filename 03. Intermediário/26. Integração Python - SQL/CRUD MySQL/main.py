import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv("USER")
senha = os.getenv("SENHA")

conexao = mysql.connector.connect(
    host='localhost',
    user=login,
    password=senha,
    database='dbcrud',
)
cursor = conexao.cursor()


#---READ---
comando = f'''
    SELECT * 
    FROM vendas
'''
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#---INSERT---
nome_produto = 'Lapis'
valor = 3
comando = f'''
    INSERT INTO vendas (nome_produto, valor)
    VALUES ("{nome_produto}"", {valor})
'''
cursor.execute(comando)
conexao.commit()

#---UPDATE---
nome_produto = 'Caneta'
valor = 7
comando = f'''
    UPDATE vendas
    SET valor = {valor}
    WHERE nome_produto = "{nome_produto}"
'''
cursor.execute(comando)
conexao.commit()

#---DELETE---
nome_produto = 'Lapis'
comando = f'''
    DELETE 
    FROM vendas
    WHERE nome_produto = "{nome_produto}"
'''
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()