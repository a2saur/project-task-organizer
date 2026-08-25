from app import create_app, db
from config import Config
from datetime import datetime, timezone

app = create_app(Config)

from app.models import Project, Task

import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
# import os

app.app_context().push()

db.create_all()
# --- Add Projects ---
proj1 = Project(
    title="Example project",
    description="An example project",
)
db.session.add(proj1)

proj2 = Project(
    title="Example project 2",
    description="An example project",
    hexColor="#eeeeff",
    official=True
)
db.session.add(proj2)

db.session.commit()

# --- Add Tasks ---
task1 = Task(
    project_id=proj1.id,
    title="Example task 1",
    description="An example task",
    completed=True,
    progress="Done",
    boardX=0.1, boardY=0.1, boardRotation=0.1, boardSize=0.1
)
db.session.add(task1)

task2 = Task(
    project_id=proj1.id,
    title="Example task 1",
    description="An example task",
    progress="Not Started",
    boardX=0.3, boardY=0.2, boardRotation=-0.1, boardSize=0.15
)
db.session.add(task2)

task3 = Task(
    project_id=proj2.id,
    title="Example task 1",
    description="An example task",
    progress="Not Started",
    boardX=0.6, boardY=0.7, boardRotation=-0.1, boardSize=0.2
)
db.session.add(task3)

db.session.commit()