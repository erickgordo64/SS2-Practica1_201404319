import pyodbc

direccion_servidor = 'WORKSTATION\SQLEXPRESS'
nombre_bd = 'Practica1'
nombre_usuario = 'WORKSTATION\erick'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';Trusted_Connection=yes')
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)