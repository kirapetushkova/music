from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class Musician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    albums = db.relationship('Album', backref='musician', lazy=True)

    def __repr__(self):
        return f"<Musician {self.name}>"

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey('musician.id'), nullable=False)

    def __repr__(self):
        return f"<Album {self.title}>"