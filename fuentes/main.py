import os
from flask import Flask, jsonify
from flask_restplus import Api, fields, Resource
from app import *
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
api = Api()
api.init_app(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
ns = api.namespace('api', description='TODO operations')
app.config['JSON_SORT_KEYS'] = False

#desde aqui se van a compenzar a llamar las rutas que se proyectaran con swagger
@ns.route('/Clients')
class getClient(Resource):
    def get(self):
        return getClients()
#Formulario que se va a proyectar en la su seccion /newClient
@api.doc(params={'rut': {'description': 'rut number is required'},
                 'v': {'description': 'rut_v number is required', 'default': None},
                 'nombre': {'description': 'name is optional', 'default': None},
                 'social_razon': {'description': 'social_razon is optional', 'default': None},
                 'date': {'description': 'date optional', 'default': None}
                 })
@ns.route('/newClient')
class newClientRoute(Resource):
    @api.doc('CustomGet with query param')
    def post(self):
        new_client = {
            "rut": request.args.get('rut'),
            "v": request.args.get('v'),
            "nombre": request.args.get('nombre'),
            "razon_social": request.args.get('social_razon'),
            "fecha_inicio_firma": request.args.get('date')
        }
        return newClient(new_client)

@api.doc(params={'rut': {'description': 'rut number is required'},
                 'nombre': {'description': 'name is optional', 'default': None},
                 'social_razon': {'description': 'social_razon is optional', 'default': None},
                 'date': {'description': 'date optional', 'default': None}
                 })
@ns.route('/editClient')
class editClientRoute(Resource):
    @api.doc('Update values from a Client')
    def put(self):
        clientValues = {
            "rut": request.args.get("rut"),
            "nombre": request.args.get("nombre"),
            "razon_social": request.args.get("social_razon"),
            "fecha_inicio_firma": request.args.get("date"),
        }
        return editClient(clientValues)

@api.doc(params={'rut': {'description': 'rut number is required'}})

@ns.route('/deleteClient')
class deleteClientRoute(Resource):
    @api.doc('Delete a Client for rut')
    def delete(self):
        rut = request.args.get("rut")
        return delClient(rut)
###############################Hasta aqui llegan las rutas de client y comienzan los de metre

@ns.route('/Metres')
class getPrueba(Resource):
    def get(self):
        return getMetres()

@api.doc(params={'rut': {'description': 'rut number is required'},
                 'id_medidor': {'description': 'id_medidor is required', 'default': None},
                 'direccion': {'description': 'direccion is optional', 'default': None},
                 'numero_instalacion': {'description': 'numero_instalacion is optional', 'default': None}
                 })
@ns.route('/addMetre')
class addMetreRoute(Resource):
    @api.doc('Add new Metre')
    def post(self):
        new_metre = {
            "ecom_id": '',
            "rut": request.args.get('rut'),
            "id_medidor": request.args.get('id_medidor'),
            "direccion": request.args.get('direccion'),
            "numero_instalacion": request.args.get('numero_instalacion')
        }
        return newMetre(new_metre)

@api.doc(params={'ecom_id': {'description': 'ecom_id number is required'},
                 'direccion': {'description': 'direccion is optional', 'default': None},
                 'numero_instalacion': {'description': 'numero_instalacion is optional', 'default': None}
                 })
@ns.route('/editMetre')
class editMetreRoute(Resource):
    @api.doc('Update values from a Metre')
    def put(self):
        metreValues = {
            "ecom_id": request.args.get('ecom_id'),
            "direccion": request.args.get('direccion'),
            "numero_instalacion": request.args.get('numero_instalacion')
        }
        return editMetres(metreValues)
        
@api.doc(params={'ecom_id': {'description': 'ecom_id number is required'}})

@ns.route('/deleteMetre')
class deleteMetreRoute(Resource):
    @api.doc('Delete a Metre for rut')
    def delete(self):
        ecom_id = request.args.get("ecom_id")
        return delMetre(ecom_id)

if __name__ == '__main__':
    app.run(debug=True, port=5000)