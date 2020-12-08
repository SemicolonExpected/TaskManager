from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    RadioField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Email, EqualTo, Length, \
    ValidationError, InputRequired

from task_manager.models.user import User


class UpdateUserForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6,
                                                                    max=35)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update')

    def __init__(self, user_name, user_email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_name = user_name
        self.user_email = user_email

    def validate_username(self, username):
        if username.data != self.user_name:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Username already exists, please use a '
                                      'unique '
                                      'username')

    def validate_email(self, email):
        if email.data != self.user_email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('Email already exists, please use a '
                                      'unique email.')


class CreateTaskForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=4, max=25)])
    #priority = RadioField('Priority', choices=['1', '2', '3', '4', '5'],
    #                      default='1', validators=[InputRequired()],
    #                      coerce=int)
    priority = RadioField('Priority', choices=['1', '2', '3', '4', '5'],
                          default='1',
                          coerce=int)
    description = StringField('Description', validators=[InputRequired()])
    try:
        start_date = DateTimeLocalField('Start Date', format='%Y-%m-%dT%H:%M', validators=[InputRequired()])
        end_date = DateTimeLocalField('End Date', format='%Y-%m-%dT%H:%M', validators=[InputRequired()])
    except Exception as e:
        start_date = None
        end_date = None

    def validate_dates(self):
        if self.start_date.data and self.end_date.data:
            if self.start_date.data >= self.end_date.data:
                return False
        return True


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=4, max=25)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6,
                                                                    max=35)])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-Enter Password',
                              validators=[DataRequired(),
                                          EqualTo('password',
                                                  message='Passwords '
                                          'do not match')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists, please use a '
                                  'unique '
                                  'username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already exists, please use a unique '
                                  'email.')
