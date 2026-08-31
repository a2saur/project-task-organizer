from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from app import db
from app.models import Project, Task, PROGRESS_OPTIONS
# from app.main.forms import CourseForm, EditForm, EmptyForm
from datetime import datetime
from . import main_bp

@main_bp.route('/', methods=['GET'])
@main_bp.route('/index', methods=['GET'])
def index():
    # courses = db.session.scalars(sqla.select(Course))
    # students = db.session.scalars(sqla.select(Student))

    return render_template('index.html', current_view='index')

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

@main_bp.route('/tasks', methods=['GET'])
def view_tasks():
    # allTasks = db.session.scalars(sqla.select(Task))
    allTasks = Task.query.order_by(Task.dueDate.asc()).all()
    return render_template('all_tasks.html', current_view='tasks', 
                           tasks=allTasks,
                           today=datetime.today(),
                           progress_opts=PROGRESS_OPTIONS)

@main_bp.route("/tasks/<int:task_id>/progress", methods=["POST"])
def update_task_progress(task_id):
    task = Task.query.get_or_404(task_id)

    data = request.get_json()
    task.progress = data["newProgress"]

    db.session.commit()

    return {"success": True}