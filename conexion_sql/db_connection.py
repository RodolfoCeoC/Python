""" import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")   #mostrar bases de datos existentes
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close() """


import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="prueba")   #mostrar tablas o registros dentro de una base de datos
cursor1=conexion1.cursor()
cursor1.execute("select * from nombres")
for tables in cursor1:
    print(tables)
conexion1.close()