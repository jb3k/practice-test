from .db import db
from flask_sclalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(20), nullable=False)
    text = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float(2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    #relationship... One post can only have 1 coffee
    coffees = db.relationship('Coffee', back_populates='posts')

    def to_dict(self):
        return {
            'id': self.id, 
            'title': self.title,
            'text': self.text,
            'coffee': self.coffees.id
            'rating': self.rating,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }

    def post_date(self):
        return {
            'createdAt': self.created_at
        }
