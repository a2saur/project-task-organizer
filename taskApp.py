# from app import create_app, db
# from config import Config
# from app.models.projects import Project, Task
# import sqlalchemy as sqla
# import sqlalchemy.orm as sqlo
# from datetime import datetime, timezone


# app = create_app(Config)

# @app.shell_context_processor
# def make_shell_context():
#     return {'sqla': sqla, 'sqlo': sqlo, 'db': db, 'Project': Project, 'Task': Task}

# if __name__ == "__main__":
#     app.run(debug=True, port=3000)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)