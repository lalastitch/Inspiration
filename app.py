from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo 

from backend.Quotes import Quotes

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Inspiration'
api = Api(app)

api.add_resource(Quotes)