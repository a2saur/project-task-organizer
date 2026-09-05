from app import db
from typing import Optional
import sqlalchemy as sqla # TODO CheckConstraint
import sqlalchemy.orm as sqlo

from datetime import datetime, timezone

class Project(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    title : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(30), unique=True)
    description : sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String(250))
    startDate : sqlo.Mapped[Optional[datetime]] = sqlo.mapped_column()
    endDate : sqlo.Mapped[Optional[datetime]] = sqlo.mapped_column()
    hexColor : sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String(7))
    official : sqlo.Mapped[bool] = sqlo.mapped_column(sqla.Boolean, default=False)
    link : sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String(100))

    # TODO: add project status
    
    # RELATIONSHIPS
    tasks : sqlo.WriteOnlyMapped['Task'] = sqlo.relationship(back_populates='project')

    # METHODS
    def get_tasks(self):
        return db.session.scalars(self.tasks.select()).all()

    def get_num_tasks(self):
        return len(db.session.scalars(self.tasks.select()).all())
    
    def get_num_completed_tasks(self):
        # TODO: improve
        allTasks = self.get_tasks()
        count = 0
        for task in allTasks:
            if task.progress == 'Done':
                count += 1
        return count

    def next_due_date(self):
        allTasks = db.session.scalars(self.tasks.select()
                                      .where(Task.progress != "Done")
                                      .where(Task.dueDate)
                                      .order_by(Task.dueDate)).all()
        if len(allTasks) > 0:
            return allTasks[0]
        else:
            return None
        
    def last_due_date(self):
        allTasks = db.session.scalars(self.tasks.select()
                                      .where(Task.progress != "Done")
                                      .where(Task.dueDate)
                                      .order_by(Task.dueDate)).all()
        if len(allTasks) > 0:
            return allTasks[-1]
        else:
            return None
        

class Task(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    project_id : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey('project.id'))
    title : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(30))
    description : sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String(250))
    dueDate : sqlo.Mapped[Optional[datetime]] = sqlo.mapped_column()
    progress : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(30))
    priority : sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String(30), default="Default")
    link : sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String(100))
    # TODO: add task types?

    boardX : sqlo.Mapped[float] = sqlo.mapped_column(sqla.Float(), default=0.0)
    boardY : sqlo.Mapped[float] = sqlo.mapped_column(sqla.Float(), default=0.0)
    boardRotation : sqlo.Mapped[float] = sqlo.mapped_column(sqla.Float(), default=0.0)
    boardSize : sqlo.Mapped[float] = sqlo.mapped_column(sqla.Float(), default=0.0)
    boardRatio : sqlo.Mapped[float] = sqlo.mapped_column(sqla.Float(), default=0.0)
    boardZ : sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer(), default=0)

    # __table_args__ = (
    #     CheckConstraint(progress.in_(['Not Started', 'In Progress', 'Almost Done', 'Done', 'Waiting on Others']), name='task_progress_check'),
    # )

    # RELATIONSHIPS
    project : sqlo.Mapped[Project] = sqlo.relationship(back_populates='tasks')
    # TODO add depends on and depended on by