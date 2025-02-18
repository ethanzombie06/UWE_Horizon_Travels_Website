from wtforms import Form, StringField, EmailField, PasswordField, validators, SubmitField, IntegerField
import email_validator


class SignUpForm(Form):
    fname = StringField('First name: ', [validators.Length(min=4, max=25)])
    lname = StringField('Last name: ', [validators.Length(min=4, max=25)])
    age = IntegerField("Age: ", [validators.NumberRange(min=18, max=130)])
    email = EmailField('Email address: ', [validators.DataRequired(), validators.Email()])
    password = PasswordField('New Password: ', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password: ')
    submit = SubmitField('Submit')

class SignInForm(Form):
    fname = StringField('First name: ', [validators.Length(min=4, max=25)])
    lname = StringField('Last name: ', [validators.Length(min=4, max=25)])
    email = EmailField('Email address: ', [validators.DataRequired(), validators.Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password: ', [validators.DataRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField('Submit')