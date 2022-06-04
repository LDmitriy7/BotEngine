from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class EditFile(FlaskForm):
    text_area = TextAreaField(label='', render_kw={'rows': 25})
    save = SubmitField('Save')
