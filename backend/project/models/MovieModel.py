from project import db
from flask_serialize import FlaskSerializeMixin

class MovieModel(db.Model, FlaskSerializeMixin):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    titleOriginal = db.Column(db.String(50))
    titlePtbr = db.Column(db.String(50))
    year = db.Column(db.Integer)


    def __repr__(self):
        return '<Movie %r> ' % self.titleOriginal