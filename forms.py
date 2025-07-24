from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, SubmitField,
                            SelectField, DateField, IntegerField, RadioField, TextAreaField)
from wtforms.validators import DataRequired, length, equal_to
from flask_wtf.file import FileField


class RegisterForm(FlaskForm):
    username = StringField("name", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired(),
                                                            length(min=8, max=32, message="password must be atleast 8 letters")])
    confirm_password = PasswordField("re password", validators=[DataRequired(),
                                                                    equal_to("password", message="passwords doesnt match")])


    submit = SubmitField("register")


class LoginForm(FlaskForm):
    username = StringField("name")
    password = PasswordField("password")
    submit = SubmitField("login")
