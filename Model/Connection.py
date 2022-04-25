#Conexion con Mysql
import mysql.connector

conexion = mysql.connector.connect(user='meli',password="meli2324!",
                                    host='localhost',
                                    database='sys',
                                    port='3306') 

print(conexion)                     