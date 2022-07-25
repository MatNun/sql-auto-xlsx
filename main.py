import mysql.connector
import os
import openpyxl

# Acessando a planilha

os.chdir("C:\\Users\\Mateus\\Documents\\code\\python\\projects\\PySQL")
workbook = openpyxl.load_workbook('senhas.xlsx')
sheet = workbook['Planilha1']
cell = sheet['A2']

# Conectando ao servidor SQL

connection = mysql.connector.connect(host='localhost',
                                     database='squid',
                                     user='root',
                                     password='123')

# While loop para adicionar cada usuário ao banco de dados

i = 4

while i <= 41:
    i += 1
    user = sheet['A' + str(i)]
    user = str(user.value)
    password = sheet['B' + str(i)]
    password = str(password.value)
    mySql_insert_query = """INSERT INTO passwd (user, password, enabled, fullname, comment) VALUES ('{}','{}','1','none','none') """.format(user, password)
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
print(cursor.rowcount, 'Record inserted successfully into database')



