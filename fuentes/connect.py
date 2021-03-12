
#Aqui se importa psycopg2 para hacer la conexion con la base de datos postgreSQL
import psycopg2
from flask import Flask, request


#conexion con la base de datos, deben de reemplazarse con los valores dependiendo del equipo

conn = psycopg2.connect(
    host = "localhost",#El nombre del host
    database = "ECOM Chile",#nombre de la base de datos, que en mi caso es ECOM CHILE
    user = 'postgres',#Nombre de usuario de la base de datos
    password = '123' #La contraseña de la base de datos
    )
#funcion que llamara a todos los clientes
def callClients():
    cursor = conn.cursor()
    cursor.execute("select * from Clientes")

    result = cursor.fetchall()
    cursor.close()
    Client=[{"rut":i[0], "v":i[1], "nombre": i[2], "razon_social": i[3],"fecha_inicio_firma": i[4]} for i in result]
    return Client
    
#Aqui se define la funcion que agregara un nuevo cliente
def addClient(client):
    cursor = conn.cursor()
    cursor.execute("insert into Clientes (rut, rut_v, nombre, razon_social, fecha_inicio_firma) values (%s,%s,%s,%s,%s);", (client['rut'],client['v'],client['nombre'],client['razon_social'],client['fecha_inicio_firma']))
    conn.commit()
    cursor.close()
#Aqui se define la funcion que agregara un nuevo Medidor
def addMetre(metre):
    cursor = conn.cursor()
    cursor.execute("insert into Medidor (ecom_id, rut, id_medidor, direccion, numero_instalacion) values (%s,%s,%s,%s,%s);", (metre['ecom_id'],metre['rut'],metre['id_medidor'],metre['direccion'],metre['numero_instalacion']))
    conn.commit()
    cursor.close()
#Aqui se define la funcion que actualizara un cliente dependiendo del rut
def updateClient(client):
    cursor = conn.cursor()
    cursor.execute("update Clientes set nombre = %s, razon_social = %s, fecha_inicio_firma = %s where rut = %s", (client['nombre'],client['razon_social'],client['fecha_inicio_firma'],client['rut']))
    conn.commit()
    cursor.close()
#Aqui se define la funcion que actualizara un medidor dependiendo del ecom_id, solo se pueden actualizar la direccion y el numero de instalacion
def updateMetre(metre):
    cursor = conn.cursor()
    cursor.execute("update Medidor set direccion = %s, numero_instalacion = %s where ecom_id = %s", (metre['direccion'],metre['numero_instalacion'],metre['ecom_id']))
    conn.commit()
    cursor.close()
#funcion que eliminara un cliente por rut
def deleteClient(rut):
    cursor = conn.cursor()
    cursor.execute("delete from Clientes where rut=%s",([rut]))
    conn.commit()
    cursor.close()
#funcion que eliminara un medidor por ecom_id
def deleteMetre(ecom_id):
    cursor = conn.cursor()
    cursor.execute("delete from Medidor where ecom_id=%s",([ecom_id]))
    conn.commit()
    cursor.close()

#funcion que llamara a todos los medidores
def callMetres():
    cursor = conn.cursor()
    cursor.execute("select * from medidor")
    metres = cursor.fetchall()
    cursor.close()
    Metre=[{"ecom_id":i[0], "rut":i[1], "id_medidor": i[2], "direccion": i[3],"numero_instalacion": i[4]} for i in metres]
    return Metre
#print(json.loads(allresult))