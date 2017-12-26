from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
from passlib.hash import bcrypt

db = SQLAlchemy()

class Entries(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(
            self,
            id=None,
            title=None,
            text=None,
            user_id=None
    ):
        self.id = id
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return "<entries(id={}, title={}, text={}, user_id={})>".format(
            self.id,
            self.title,
            self.text,
            self.user_id
        )

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    entries = db.relationship('Entries', backref='user', lazy=True)

    def __init__(
            self,
            id=None,
            name=None,
            password=None
    ):
        self.id = id
        self.name = name
        self.password = bcrypt.encrypt(password)

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return "<users(id={}, name={}, password={})>".format(
            self.id,
            self.name,
            self.password
        )