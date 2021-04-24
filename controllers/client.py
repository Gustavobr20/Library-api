from flask import request
from flask_restplus import Resource, fields

from models.client import ClientModel
from schema.client import ClientSchema

from server.instance import server

client_ns = server.client_ns

client_schema = ClientSchema()
client_list_schema = ClientSchema(many=True)

CLIENT_NOT_FOUND = 'Cliente não encontrado!'

client = client_ns.model('Client', {
    'name': fields.String(description='full name')
})


class Client(Resource):

    def get(self, id):
        client_data = ClientModel.find_by_id(id)
        if client_data:
            return client_schema.dump(client_data), 200

    @client_ns.expect(client)
    def put(self, id):
        client_data = ClientModel.find_by_id(id)
        client_json = request.get_json()

        client_data.name = client_json['name']

        client_data.save_to_db()
        return client_schema.dump(client_data), 200

    def delete(self, id):
        client_data = ClientModel.find_by_id(id)
        if client_data:
            client_data.delete_from_db()
            return '', 204
        return {'message': CLIENT_NOT_FOUND}


class ClientList(Resource):
    def get(self):
        return client_list_schema.dump(ClientModel.find_all()), 200

    @client_ns.expect(client)
    @client_ns.doc('Create an Client')
    def post(self):
        client_json = request.get_json()
        client_data = client_schema.load(client_json)

        client_data.save_to_db()

        return client_schema.dump(client_data), 201
