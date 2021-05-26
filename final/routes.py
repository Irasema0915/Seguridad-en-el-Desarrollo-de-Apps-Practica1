from flask import jsonify
from flask_restful import Resource, reqparse
from models import UsuarioModel
from conf import db

#argumentos/parametros para tomar de los requests
args_usuario = reqparse.RequestParser()
args_usuario.add_argument('name',type=str)
args_usuario.add_argument('email',type=str)
args_usuario.add_argument('password',type=str)

#clase con los métodos de las rutas por verbos(GET, POST)
class UsuarioRoutes(Resource):
    def get(self):
        try:
            response = UsuarioModel.query.all()
            response = [{
                'id':i.id,
                'name':i.name,
                'email':i.email,
                'password':i.password,
                'created_at':i.created_at,
                'updated_at':i.updated_at} for i in response]
            return jsonify(response)
        except:
            return {
                'error' : 'Error al obtener los usuarios flask'
            }

    def post(self):
        try:
            args = args_usuario.parse_args()
            usuario = UsuarioModel(
                            name = args.name,
                            email = args.email,
                            password = args.password)
            db.session.add(usuario)
            db.session.commit()
            return {
                'message' : 'Usuario ' + usuario.name +' agregado correctamente.'
            }, 201
        except:
            return {
                'message' : 'Error al registrar el usuario'
            }