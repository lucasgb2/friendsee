from flask import Flask
from flask_cors import CORS
from flask_migrate import  Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(cfg):      
    app = Flask(__name__)            
    app.config.from_object(cfg)    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'        
    
    CORS(app)
    
    db.init_app(app)

    from .models import MovieModel
    from .routes.MovieRoutes import bpMovie

    migrate = Migrate(app, db)    
    app.register_blueprint(bpMovie, url_prefix='/api/movie')
    return app





