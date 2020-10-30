from datetime import datetime
from ..__init__ import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


'''
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from ..__init__ import db


class Task(db.Model):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True, nullable=False)
    priority = Column(Integer, default=1, nullable=False)
    description = Column(Text, unique=True, nullable=True)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    time_estimate = Column(String(80), nullable=True)

    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return '<Task {} {}>'.format(self.title, self.priority)
'''
