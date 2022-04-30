#Conexion con Mysql
import mysql.connector
from Controller.Login import login
conexion = mysql.connector.connect(user='root',password="meli2324!",
                                    host='localhost',
                                    database='sys',
                                    port='3306') 

print(conexion)                     





#Listando Todos los archivos de root Folder (mi drive)

# Auto-iterate through all files that matches this query

credenciales = login()
#'q' la necesito para especificar una consulta, esto es de drive
file_list = credenciales.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list: #file1 donde guardo una sola celda, y file list, la celda completa
    #en la %s es el posible string futuro, luego lo reemplazo con el valor actuar de file1, el title
    print('title: %s, id: %s' % (file1['title'], file1['id']) + '   ' + file1['fileExtension'] + '   ' + str(file1['shared']  ) + '   '  + file1['modifiedDate']    )

    for elemento in file1['ownerNames']:
        print(elemento)

    

