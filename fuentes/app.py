from flask import Flask, jsonify, request
from connect import *

#Congifuracion para evitar que ordene el json 
app = Flask(__name__)

#Funcion que muestra los clientes con su respectiva ruta
def getClients():
    clients = callClients()
    return jsonify({"Clients": clients})

#Funcion que muestra los medidores con su respectiva ruta
def getMetres():
    metres = callMetres()
    return jsonify({"Metres": metres})

#Funcion que agrega un nuevo Cliente en la ruta /Clients
def newClient(client):
    addClient(client)
    return jsonify({"message":"Product Added Succesfully"})
#Funcion que agrega un nuevo medidor en la ruta /Metres
def newMetre(metre):
    addMetre(metre)
    return jsonify({"message":"Product Added Succesfully"})
#Esta funcion se encarga de llamar editClient para actualizar un cliente por su rut en la ruta /Clients
def editClient(client):
    updateClient(client)
    return jsonify({"message":"Product Updated"})
#Esta funcion se encarga de llamar editMetres para actualizar un medidor por su ecom_id en la ruta /Metres
def editMetres(metre):
    updateMetre(metre)
    return jsonify({"message":"Product Updated"})
#esta funcion se encarga de llamar deleteMetre para poder eliminar un medidor por su ecom_id

def delMetre(ecom_id):
    deleteMetre(ecom_id)
    return jsonify({"message":"Delete Succesfully"})
#esta funcion se encarga de llamar deleteClient para poder eliminar un Cliente por su rut

def delClient(rut):
    deleteClient(rut)
    return jsonify({"message":"Delete Succesfully"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)


