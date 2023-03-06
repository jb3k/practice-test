from .db import db
from flask_sclalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Coffee(db.Model):
    __tablename__ = 'coffee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    caffine_content = db.Column(db.Float(2), nullable=False)
    caffine_percentage = db.Column(db.Float(2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    #relationship... One coffee can have many posts
    posts = db.relationship('Post', back_populates='coffees')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'caffine_content': self.caffine_content,
            'caffine_percentage': self.caffine_percentage,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }
