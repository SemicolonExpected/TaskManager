# from flask_restx import Resource, Api
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from ..__init__ import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
