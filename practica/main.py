from menu import *
from bd import conexion
import os

def main():
    menuPrint()

def menuPrint():
    opcion = None
    while opcion != "7":
        print_main_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("SE PROCEDERA A BORRAR LA BASE DE DATOS")
            borraTablas()
        elif opcion == "2":
            print("SE PROCEDERA A CREAR EL MODELO DE LA BD")
            creaModelo()
        elif opcion == "3":
            print("SE PROCEDERA A REALIZAR AL CARGA MASIVA")
            cargaMasiva()
        elif opcion == "4":
            print("SE PROCEDERA A REALIZAR LIMIEZA DE DATA")
            limpiarData()
        elif opcion == "5":
            print("CARGA DE INFORMACION EN LA BASE DE DATOS")
            llenaBD()
        elif opcion == "6":
            print("REALIZANDO LAS CONSULTAS DE LA PRACTICA")
            consultas()
        elif opcion == "7":
            conexion.close()
            exit()
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

def borraTablas():
    try:
        ruta_archivo_sql = os.path.join('practica','eliminado', 'eliminado.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                conexion.commit()
    except Exception as e:
                print("Ocurrió un al eliminar la bd: ", e) 

def creaModelo():
    try:
        ruta_archivo_sql = os.path.join('practica','ddl', 'creacionbd.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                conexion.commit()
    except Exception as e:
                print("Ocurrió un error al crear la bd: ", e) 

def cargaMasiva():
    try:
        ruta_archivo_sql = os.path.join('practica','dml', 'cargamasiva.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                conexion.commit()
    except Exception as e:
                print("Ocurrió un error al consultar: ", e) 

def llenaBD():
    try:
        ruta_archivo_sql = os.path.join('practica','dml', 'llenadotablas.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                conexion.commit()
    except Exception as e:
                print("Ocurrió un error al consultar: ", e) 

def limpiarData():
    try:
        ruta_archivo_sql = os.path.join('practica','limpieza', 'limpiezaData.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                conexion.commit()
    except Exception as e:
                print("Ocurrió un error al consultar: ", e) 

def consultas():
    print("--------- consulta 1 -----------")
    consulta1()
    print("--------- consulta 2 -----------")
    consulta2()
    print("--------- consulta 3 -----------")
    consulta3()
    print("--------- consulta 4 -----------")
    consulta4()
    print("--------- consulta 5 -----------")
    consulta5()
    print("--------- consulta 6 -----------")
    consulta6()
    print("--------- consulta 7 -----------")
    consulta7()
    print("--------- consulta 8 -----------")
    consulta8()
    print("--------- consulta 9 -----------")
    consulta9()
    print("--------- consulta 10 -----------")
    consulta10()

def consulta1():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta1.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            consultas = contenido_sql.split(';')
            cursor = conexion.cursor()
            for consulta in consultas:
                consulta = consulta.strip()  # Elimina espacios en blanco
                if consulta:  # Ignora líneas vacías
                    cursor.execute(consulta)
                    resultados = cursor.fetchall()

                    for fila in resultados:
                        print(f"Fila: {fila}")
                        texto += f"Fila: {fila}\n"
                    texto = texto + "------------\n"
        crearArchivo(texto, "consulta1.txt")
        
    except Exception as e:
                print("Ocurrió un error al consultar: ", e)

def consulta2():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta2.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                Datos = cursor.fetchall()

                for Dato in Datos:
                    print(Dato)
                    texto += f"Fila: {Dato}\n"
        crearArchivo(texto, "consulta2.txt")
    except Exception as e:
                print("Ocurrió un error al consultar: ", e)

def consulta3():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta3.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                Datos = cursor.fetchall()

                for Dato in Datos:
                    print(Dato)
                    texto += f"Fila: {Dato}\n"
        crearArchivo(texto, "consulta3.txt")
    except Exception as e:
                print("Ocurrió un error al consultar: ", e)

def consulta4():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta4.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                Datos = cursor.fetchall()

                for Dato in Datos:
                    print(Dato)
                    texto += f"Fila: {Dato}\n"
        crearArchivo(texto, "consulta4.txt")
    except Exception as e:
                print("Ocurrió un error al consultar: ", e)

def consulta5():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta5.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                Datos = cursor.fetchall()

                for Dato in Datos:
                    print(Dato)
                    texto += f"Fila: {Dato}\n"
        crearArchivo(texto, "consulta5.txt")
    except Exception as e:
                print("Ocurrió un error al consultar: ", e)

def consulta6():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta6.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                Datos = cursor.fetchall()

                for Dato in Datos:
                    print(Dato)
                    texto += f"Fila: {Dato}\n"
        crearArchivo(texto, "consulta6.txt")
    except Exception as e:
                print("Ocurrió un error al consultar: ", e)

def consulta7():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta7.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                Datos = cursor.fetchall()

                for Dato in Datos:
                    print(Dato)
                    texto += f"Fila: {Dato}\n"
        crearArchivo(texto, "consulta7.txt")
    except Exception as e:
                print("Ocurrió un error al consultar: ", e)

def consulta8():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta8.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                Datos = cursor.fetchall()

                for Dato in Datos:
                    print(Dato)
                    texto += f"Fila: {Dato}\n"
        crearArchivo(texto, "consulta8.txt")
    except Exception as e:
                print("Ocurrió un error al consultar: ", e) 

def consulta9():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta9.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                Datos = cursor.fetchall()

                for Dato in Datos:
                    print(Dato)
                    texto += f"Fila: {Dato}\n"
        crearArchivo(texto, "consulta9.txt")
    except Exception as e:
                print("Ocurrió un error al consultar: ", e)

def consulta10():
    try:
        texto = ""
        ruta_archivo_sql = os.path.join('practica','consultas', 'consulta10.sql')
        with open(ruta_archivo_sql, 'r') as sql_file:
            contenido_sql = sql_file.read()
            with conexion.cursor() as cursor:
                cursor.execute(contenido_sql)
                Datos = cursor.fetchall()

                for Dato in Datos:
                    print(Dato)
                    texto += f"Fila: {Dato}\n"
        crearArchivo(texto, "consulta10.txt")
    except Exception as e:
                print("Ocurrió un error al consultar: ", e)

def crearArchivo(texto, nombre_archivo):
    # Abrir un archivo en modo escritura
    with open(nombre_archivo, "w") as archivo:
        # Escribir el texto en el archivo
        archivo.write(texto)

if __name__ == "__main__":
    main()