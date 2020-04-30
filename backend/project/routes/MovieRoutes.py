from flask import  Blueprint, jsonify, request, json

from project import db
from project.models.MovieModel import MovieModel

bpMovie = Blueprint('movie', __name__)

@bpMovie.route('/', methods=['GET'])
def index():
    #obj = MovieModel(titleOriginal='The Lord of the Rings', titlePtbr='O Senhor dos Anéis',year=2001)    
    #db.session.add(obj)
    #db.session.commit()

    
    v = MovieModel.get_delete_put_post()
    print(v)
    return v

@bpMovie.route('/', methods=['POST'])
def post():
    return jsonify({"message":"ola"})    

@bpMovie.route('/', methods=['UPDATE'])
def update():
    return jsonify({"message":"ola"})    

@bpMovie.route('/<int:id>', methods=['DELETE'])
def delete():
    return jsonify({"message":"ola"})

