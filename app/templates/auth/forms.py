from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class ReviewForm(FlaskForm):

    
    pitch = TextAreaField('Create pitch ', validators=[Required()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class ReviewForm(FlaskForm):

    
    comments = TextAreaField('comments', validators=[Required()])
    submit = SubmitField('Submit')
