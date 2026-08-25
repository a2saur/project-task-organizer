from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from app import db
from app.models import Project, Task
# from app.main.forms import CourseForm, EditForm, EmptyForm
from . import main_bp

@main_bp.route('/', methods=['GET'])
@main_bp.route('/index', methods=['GET'])
def index():
    # courses = db.session.scalars(sqla.select(Course))
    # students = db.session.scalars(sqla.select(Student))

    return render_template('index.html')

# @main.route('/course/create', methods=['GET', 'POST'])
# def create_course():
#     cform = CourseForm()
#     if cform.validate_on_submit():
#         newCourse = Course(major_id=cform.major.data.id, 
#                             coursenum=cform.coursenum.data, 
#                             title=cform.title.data)
#         db.session.add(newCourse)
#         db.session.commit()
#         flash("Course \""+newCourse.get_major().get_name()+" - "+newCourse.get_coursenum()+"\" has been created")
#         return redirect(url_for('main.index'))
#     return render_template('create_course.html', form = cform)

