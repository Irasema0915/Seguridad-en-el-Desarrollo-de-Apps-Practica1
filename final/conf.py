from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

#iniciar app
app = Flask(__name__)
api = Api(app)

#conf de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Irasema.0915@localhost:5432/conexion'
db = SQLAlchemy(app)