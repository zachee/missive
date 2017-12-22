from flask_sqlalchemy import SQLAlchemy 
from flask import Flask

db = SQLAlchemy()

class Entries(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(
            self,
            id=None,
            title=None,
            text=None
    ):
        self.id = id
        self.title = title
        self.text = text

    def __repr__(self):
        return "<entries(id={}, title={}, text={}, email={}, title={}, created={})>".format(
            self.id,
            self.title,
            self.text
        )
