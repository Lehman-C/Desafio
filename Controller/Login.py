""" importamos dependencias, google auth que para poder hacer la autenticacion y tambien el object google drive que
permite traerme todas las funciones del api de google drive """
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

#guardo el path en una variable
path_credential = 'Controller\\credentials_module.json'

#Iniciar Sesion - funcion,instanciando el objeto google auth
def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(path_credential)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(path_credential)
        print("Token expirado, Volve a Ejecutar")
    else:
        gauth.Authorize()
        return GoogleDrive(gauth)








""" #Descargar 

def descargar_archivo(id_archivo,ruta_descarga):
    credenciales = login()
    archivo = credenciales.CreateFile({'id': id_archivo})
    nombre_archivo = archivo['title']
    archivo.GetContentFile(ruta_descarga + nombre_archivo)
    
if __name__ == "__main__":  #Cuando el interprete ejecuta el modulo(archivo) de python a la variable especial __name__ le da el valor __main__
    descargar_archivo('119lCvQPOPIhWXPEry0nj5yvl9WyL9NFF','C:\\Users\\JOSE\\Desktop\\Desafio\\')

 """