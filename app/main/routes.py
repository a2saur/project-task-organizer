from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from app import db
from app.models import Project, Task, PROGRESS_OPTIONS
from app.main.forms import TaskForm
from datetime import datetime
from . import main_bp

import random

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

@main_bp.route("/tasks/add", methods=['GET', 'POST'])
def add_task():
    tForm = TaskForm()
    if tForm.validate_on_submit():
        newTask = Task(
            project_id=tForm.project.data.id,
            title=tForm.title.data,
            description=tForm.description.data,
            progress=tForm.progress.data,
            priority=tForm.priority.data,
            boardX=random.random()*0.9, boardY=random.random()*0.9,
            boardRotation=(random.random()*0.2)-0.1, boardSize=(random.random()*0.1)+0.1, boardRatio=(random.random()*0.2)+0.6
        )
        if tForm.dueDate.data != "":
            newTask.dueDate = datetime.strptime(tForm.dueDate.data, "%m/%d/%y %H:%M")
        db.session.add(newTask)
        db.session.commit()
        return redirect(url_for("main.view_tasks"))
    return render_template("add_task.html", current_view="add_task",
                           tForm=tForm)

@main_bp.route("/tasks/edit/<int:task_id>", methods=['GET', 'POST'])
def edit_task(task_id):
    editTask = db.session.get(Task, task_id)
    if editTask.dueDate:
        dueDate = editTask.dueDate.strftime("%m/%d/%y %H:%M")
    else:
        dueDate = ""
    if request.method == "GET":
        tForm = TaskForm(
            title=editTask.title,
            description=editTask.description,
            dueDate=dueDate,
            priority=editTask.priority,
            progress=editTask.progress
        )
    else:
        tForm = TaskForm()

    if tForm.validate_on_submit():
        editTask.project_id = tForm.project.data.id
        editTask.title = tForm.title.data
        editTask.description = tForm.description.data
        editTask.progress = tForm.progress.data
        editTask.priority = tForm.priority.data
        if tForm.dueDate.data != "":
            editTask.dueDate = datetime.strptime(tForm.dueDate.data, "%m/%d/%y %H:%M")
        else:
            editTask.dueDate = None
        db.session.commit()
        return redirect(url_for("main.view_tasks"))

    return render_template("add_task.html", current_view="add_task",
                               tForm=tForm)