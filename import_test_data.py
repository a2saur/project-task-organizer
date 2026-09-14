from app import create_app, db
from config import Config
from datetime import datetime, timezone

app = create_app(Config)

from app.models import Project, Task

import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

import pandas as pd
import random

# --- Read data ---
df = pd.read_csv("setup-files/todos.csv")
# projectDeets = pd.read_csv("setup-files/projects.csv")


app.app_context().push()

db.create_all()
# --- Add Projects ---
projects = {}
for projName in set(df["project"]):
    # projDeets = projectDeets.loc[projectDeets["name"] == projName]
    proj = Project(
        title=projName,
        official=True
        # description=projDeets["description"],
        # hexColor=projDeets["hex_color"],
        # official=projDeets["official"],
    )
    projects[projName] = proj
    db.session.add(proj)

db.session.commit()

# --- Add Tasks ---
for index, taskInfo in df.iterrows():
    task = Task(
        project_id=projects[taskInfo["project"]].id,
        title=taskInfo["task"],
        description="",
        progress=taskInfo["status"],
        boardX=random.random()*0.9, boardY=random.random()*0.9,
        boardRotation=(random.random()*0.2)-0.1, boardSize=(random.random()*0.1)+0.1, boardRatio=(random.random()*0.2)+0.6
    )
    if type(taskInfo["priority"]) == str:
        task.priority = taskInfo["priority"]
    if type(taskInfo["due date"]) == str:
        # task.dueDate = datetime.strptime(taskInfo["due date"], "%m/%d/%y %H:%M")
        task.set_due_date(taskInfo["due date"])
    db.session.add(task)

db.session.commit()