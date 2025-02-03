from wtforms import Form, StringField, EmailField, PasswordField, validators, SubmitField
import email_validator


class SignUpForm(Form):
    username = StringField('Username: ', [validators.Length(min=4, max=25)])
    email = EmailField('Email address: ', [validators.DataRequired(), validators.Email()])
    password = PasswordField('New Password: ', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password: ')
    submit = SubmitField('Submit')

class SignInForm(Form):
    username = StringField('Username: ', [validators.Length(min=4, max=25)], render_kw={"placeholder": "Username"})
    email = EmailField('Email address: ', [validators.DataRequired(), validators.Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password: ', [validators.DataRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField('Submit')