from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch body')
    category = SelectField(choices=[('coding', 'coding'),('technology','technology'),('deals','deals')])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Say something avout this', validators=[Required()])



