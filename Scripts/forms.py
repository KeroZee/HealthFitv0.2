from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms.fields.html5 import DateField
from wtforms import StringField, PasswordField, IntegerField, RadioField, BooleanField, FloatField, SubmitField, TextAreaField, SelectField
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

        user = User.query.filter_by(username=username.data.lower()).first()

        if user:
            raise ValidationError('That username is taken. Please Choose a different one')
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data.lower()).first()

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
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    weight = IntegerField('Weight (KG)')
    height = FloatField('Height (M)')
    age = IntegerField('Age')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data.lower()).first()
            if user:
                raise ValidationError('That username is taken. Please Choose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data.lower()).first()
            if user:
                raise ValidationError('That email is taken. Please Choose a different one')
class TodoList(FlaskForm):
    datetime = DateField('Date', format='%Y-%m-%d')
    description = TextAreaField('Description', validators=[DataRequired()], render_kw={"placeholder":"Enter your to-do in this section\nExample: Do 4 sets of 10 push-ups everyday starting from 26 January 2019"})
    remarks = TextAreaField('Remarks', render_kw={"placeholder":"Enter any important info about your to-dos\nExample: To train for stomach muscles"})
    submit = SubmitField('Add')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6, max=50)])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data.lower()).first()
        if user is None:
            raise ValidationError('There is no account linked to that email. Please Enter valid email.')

class ResetPasswordForm(FlaskForm):

    password = PasswordField('Password',
        validators=[DataRequired(), EqualTo('password'),Length(min=6, max=24)])
    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class FoodForm(FlaskForm):
    name = StringField('Food',validators=[DataRequired()])
    mass = IntegerField('Mass',validators=[DataRequired()])
    calories = IntegerField('Calories',validators=[DataRequired()])
    protein = IntegerField('Protein',validators=[DataRequired()])
    carbohydrates = IntegerField('Carbs',validators=[DataRequired()])
    fats = IntegerField('Fats',validators=[DataRequired()])
    submit = SubmitField('Add Food')

class ExerciseForm(FlaskForm):
    name = StringField('Exercise',validators=[DataRequired()])
    duration = IntegerField('Duration',validators=[DataRequired()])
    intensity = IntegerField('Reps',validators=[DataRequired()])
    submit = SubmitField('Add Exercise')

class SearchForm(FlaskForm):
    meal = SelectField('Meal : ', choices=[('breakfast','Breakfast'),('lunch','Lunch'),('dinner','Dinner')])
    name = StringField('Food Name',validators=[DataRequired()])
    submit = SubmitField('Search & Add')

class HealthForm(FlaskForm):
    heartrate = StringField('Food Name',validators=[DataRequired()])
    submit = SubmitField('Measure')

