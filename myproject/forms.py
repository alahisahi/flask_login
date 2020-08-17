from  flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('login')

class Registration(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='password must match')])
    pass_confirm=PasswordField("confirm password",validators=[DataRequired()])
    submit=SubmitField('register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('ur email has been already registered')


    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('user name already taken')
