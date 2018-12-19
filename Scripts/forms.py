from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, IntegerField, RadioField, BooleanField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from Scripts.models import User

class RegisterForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=1, max=50)])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6, max=50)])
    password = PasswordField('Password',
        validators=[DataRequired(), EqualTo('password'),Length(min=6, max=24)])
    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    weight = IntegerField('Weight (KG)')
    height = FloatField('Height (M)')
    gender = RadioField('Gender',choices = [('M','Male'),('F','Female')])
    age = IntegerField('Age')
    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is taken. Please Choose a different one')
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That email is taken. Please Choose a different one')

class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password',
        validators=[DataRequired(), EqualTo('password')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateDetails(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6, max=50)])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please Choose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please Choose a different one')
