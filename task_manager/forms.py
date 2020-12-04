from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    RadioField, DateField, TimeField
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


class CreateTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),
                                             Length(min=4, max=25)])
    priority = RadioField('Priority', choices=['1', '2', '3', '4', '5'],
                          default='1', validators=[InputRequired()],
                          coerce=int)
    description = StringField('Description', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    end_time = TimeField('End Time', validators=[DataRequired()])

    @property
    def start(self):
        if self.start_date.data and self.start_time.data:
            return datetime.combine(self.start_date.data, self.start_time.data)

    @property
    def end(self):
        if self.end_date.data and self.end_time.data:
            return datetime.combine(self.end_date.data, self.end_time.data)

    # def validate_end_date(self, field):
    #     if self.start > self.end:
    #         raise ValidationError("End date must be after start date.")


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
