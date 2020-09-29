from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    
    description = TextAreaField('create blog', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment= TextAreaField('make comments', validators=[Required()])
    submit = SubmitField('Submit')

class SubscriptionForm(FlaskForm):

    email= TextAreaField('Enter your Email', validators=[Required()])
    submit = SubmitField('Submit')
