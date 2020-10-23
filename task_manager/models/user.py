from task_manager import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

from task_manager import db, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {} {} {}>'.format(
            self.username, self.email, self.password)
