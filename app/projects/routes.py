from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from . import projects_bp

from app import db
from app.models import Project, Task, PROGRESS_OPTIONS
from app.main.forms import ProjectForm

from datetime import datetime

@projects_bp.route('/projects', methods=['GET'])
def view_projects():
    projects = db.session.scalars(sqla.select(Project))

    return render_template('projects.html', current_view='projects',
                           projects=projects)

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

@projects_bp.route("/projects/<int:project_id>", methods=['GET'])
def view_project(project_id):
    project = db.session.get(Project, project_id)
    return render_template('project.html', current_view='projects',
                               project=project,
                               today=datetime.today(),
                               tasks=project.get_tasks(),
                               progress_opts=PROGRESS_OPTIONS)

@projects_bp.route("/projects/add", methods=['GET', 'POST'])
def add_project():
    pForm = ProjectForm()
    if pForm.validate_on_submit():
        newProject = Project(
            title=pForm.title.data,
            description=pForm.description.data,
            hexColor=pForm.colorPicked.data,
            official=pForm.official.data,
        )
        if pForm.startDate.data != "":
            newProject.startDate = datetime.strptime(pForm.startDate.data, "%m/%d/%y %H:%M")
        if pForm.endDate.data != "":
            newProject.startDate = datetime.strptime(pForm.endDate.data, "%m/%d/%y %H:%M")
        db.session.add(newProject)
        db.session.commit()
        return redirect(url_for("projects.view_projects"))
    return render_template("add_project.html", current_view="add_project",
                           pForm=pForm)

@projects_bp.route("/projects/edit/<int:project_id>", methods=['GET', 'POST'])
def edit_project(project_id):
    editProject = db.session.get(Project, project_id)
    if editProject.endDate:
        endDate = editProject.startDate.strftime("%m/%d/%y %H:%M")
    else:
        endDate = ""
    if editProject.startDate:
        startDate = editProject.startDate.strftime("%m/%d/%y %H:%M")
    else:
        startDate = ""
    if request.method == "GET":
        pForm = ProjectForm(
            title=editProject.title,
            description=editProject.description,
            startDate=startDate,
            endDate=endDate,
            colorPicked=editProject.hexColor,
            official=editProject.official,
        )
    else:
        pForm = ProjectForm()

    if pForm.validate_on_submit():
        editProject.title = pForm.title.data
        editProject.description = pForm.description.data
        if pForm.startDate.data != "":
            editProject.startDate = datetime.strptime(pForm.startDate.data, "%m/%d/%y %H:%M")
        else:
            editProject.startDate = None
        if pForm.endDate.data != "":
            editProject.endDate = datetime.strptime(pForm.endDate.data, "%m/%d/%y %H:%M")
        else:
            editProject.endDate = None
        if pForm.colorPicked.data != "":
            editProject.hexColor = pForm.colorPicked.data
        editProject.official = pForm.official.data
        db.session.commit()
        return redirect(url_for("projects.view_projects"))

    return render_template("add_project.html", current_view="add_project",
                           pForm=pForm)