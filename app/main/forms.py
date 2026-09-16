from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, ColorField, SelectField, SubmitField
from wtforms.validators import  Length, DataRequired, EqualTo, Email, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField

from app import db
from app.models import Project, PROGRESS_OPTIONS, PRIORITIES
import sqlalchemy as sqla

class ProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    description = StringField('Project Description')
    startDate = StringField('Start Date (m/d/y)')
    link = StringField('Link for task')
    endDate = StringField('End Date (m/d/y)')
    colorPicked = ColorField("Project Color")
    official = BooleanField("Official? ")
    submit = SubmitField('Save')

class TaskForm(FlaskForm):
    project = QuerySelectField('Project',
                             query_factory = lambda : db.session.scalars(sqla.select(Project)),
                             get_label = lambda proj : proj.title,
                             allow_blank = False)
    title = StringField('Task Name', validators=[DataRequired()])
    description = StringField('Task Description')
    link = StringField('Link for task')
    dueDate = StringField('Due Date (m/d/y H:M)')
    priority = SelectField(
        'Priority',
        choices=PRIORITIES,
        default=PRIORITIES[0]
    )
    progress = SelectField(
        'Progress',
        choices=PROGRESS_OPTIONS,
        default=PROGRESS_OPTIONS[0]
    )
    softDeadline = BooleanField("Soft Deadline")
    submit = SubmitField('Save')
