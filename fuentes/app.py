from flask import Flask, jsonify, request
from connect import *

#Congifuracion para evitar que ordene el json 
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#Funcion que muestra los clientes con su respectiva ruta
@app.route('/Clients')
def getClients():
    clients = callClients()
    return jsonify({"Clients": clients})

#Funcion que muestra los medidores con su respectiva ruta
@app.route('/Metres')
def getMetres():
    metres = callMetres()
    return jsonify({"Metres": metres})

#Funcion que agrega un nuevo Cliente en la ruta /Clients
@app.route('/Clients', methods=['POST'])
def newClient():
    new_Client = {
        "rut": request.json['rut'],
        "v": request.json["v"],
        "nombre": request.json["nombre"],
        "razon_social": request.json["razon_social"],
        "fecha_inicio_firma": request.json["fecha_inicio_firma"],
    }
    addClient(new_Client)
    return jsonify({"message":"Product Added Succesfully"})
#Funcion que agrega un nuevo medidor en la ruta /Metres
@app.route('/Metres', methods=['POST'])
def newMetre():
    new_Metre = {
        "ecom_id": '',
        "rut": request.json["rut"],
        "id_medidor": request.json["id_medidor"],
        "direccion": request.json["direccion"],
        "numero_instalacion": request.json["numero_instalacion"],
    }
    addMetre(new_Metre)
    return jsonify({"message":"Product Added Succesfully"})
#Esta funcion se encarga de llamar editClient para actualizar un cliente por su rut en la ruta /Clients
@app.route('/Clients/<int:rut>', methods=['PUT'])
def editClient(rut):
    clientValues = {
        "rut": rut,
        "nombre": request.json["nombre"],
        "razon_social": request.json["razon_social"],
        "fecha_inicio_firma": request.json["fecha_inicio_firma"],
    }
    updateClient(clientValues)
    return jsonify({"message":"Product Updated"})
#Esta funcion se encarga de llamar editMetres para actualizar un medidor por su ecom_id en la ruta /Metres
@app.route('/Metres/<string:ecom_id>', methods=['PUT'])
def editMetres(ecom_id):
    metreValues = {
        "ecom_id": ecom_id,
        "direccion": request.json["direccion"],
        "numero_instalacion": request.json["numero_instalacion"],
    }
    updateMetre(metreValues)
    return jsonify({"message":"Product Updated"})
#esta funcion se encarga de llamar deleteMetre para poder eliminar un medidor por su ecom_id
@app.route('/Metres/<string:ecom_id>', methods=['DELETE'])
def delMetre(ecom_id):
    deleteMetre(ecom_id)
    return jsonify({"message":"Delete Succesfully"})
#esta funcion se encarga de llamar deleteClient para poder eliminar un Cliente por su rut
@app.route('/Clients/<int:rut>', methods=['DELETE'])
def delClient(rut):
    deleteClient(rut)
    return jsonify({"message":"Delete Succesfully"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)


