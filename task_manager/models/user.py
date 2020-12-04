from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

from task_manager import db, login, ma
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<User {} {} {}>'.format(
            self.id, self.username, self.email)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
