from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import  Length, DataRequired, EqualTo, Email, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

from app import db
# from app.models
import sqlalchemy as sqla

# class CourseForm(FlaskForm):
#     coursenum = StringField('Course Number',[Length(min=3, max=6)])
#     title = StringField('Course Title', validators=[DataRequired()])
#     major = QuerySelectField('Major',
#                              query_factory = lambda : db.session.scalars(sqla.select(Major)),
#                              get_label = lambda theMajor : theMajor.name,
#                              allow_blank = False)
#     submit = SubmitField('Post')
