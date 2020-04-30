from flask import  Blueprint, jsonify, request, json, request, abort

from project import db
from project.models.MovieModel import MovieModel

bpMovie = Blueprint('movie', __name__)

@bpMovie.route('/', methods=['GET'])
def index():    
    return MovieModel.get_delete_put_post()

@bpMovie.route('/', methods=['POST'])
def post():
    print(request.data)
    #https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
    return "ok"

@bpMovie.route('/', methods=['UPDATE'])
def update():
    return jsonify({"message":"ola"})    

@bpMovie.route('/<int:id>', methods=['DELETE'])
def delete():
    return jsonify({"message":"ola"})

