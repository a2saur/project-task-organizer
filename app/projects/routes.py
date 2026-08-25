from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from . import projects_bp

from app import db
from app.models import Project, Task
# from app.main.forms import CourseForm, EditForm, EmptyForm

@projects_bp.route('/projects', methods=['GET'])
def view_projects():
    projects = db.session.scalars(sqla.select(Project))

    return render_template('projects.html',
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

@projects_bp.route("/projects/<int:project_id>")
def view_project(project_id):
    project = db.session.get(Project, project_id)
    return render_template('project.html',
                               project=project,
                               tasks=project.get_tasks())