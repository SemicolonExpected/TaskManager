from werkzeug.security import generate_password_hash, check_password_hash

from task_manager import db, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {} {} {}>'.format(self.username, self.email, self.password)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
