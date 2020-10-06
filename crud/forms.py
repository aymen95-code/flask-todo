from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, Length

class TodoForm(FlaskForm):
    content = StringField('Add a new item', [validators.Length(min=2, max=10), validators.DataRequired()])
    submit = SubmitField('submit')
